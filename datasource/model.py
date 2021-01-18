from abc import ABC, abstractmethod
from typing import List
from datasource.gateway import IQGateway
from datasource.oracle import create_connection, create_connection2, run_query_many
import pandas as pd
import os
import time

class DataSource(ABC):

    @abstractmethod
    def get_list_of_table_names(self):
        pass

    @abstractmethod
    def get_table(self, table_name: str):
        pass

    @abstractmethod
    def get1000notnullrows(self, table_name: str):
        pass

    @abstractmethod
    def save_table(self, table_name: str, df: pd.core.frame.DataFrame):
        pass


class IQDataSource(DataSource):

    def __init__(self, name, gateway: IQGateway):
        self.name = name
        self._gateway = gateway

    def get_list_of_table_names(self) -> List[str]:
        return self._gateway.get_list_of_table_names()

    # def get_table(self, table_name: str):
    #     # todo-high-prusove нужно доработать функцию, чтобы она возвращала df с chunk-ами
    #     rows = self._gateway.get_table_rows(table_name=table_name)
    #     if rows is not None:
    #         columns = [column_meta[0] for column_meta in rows.description]
    #         df = pd.DataFrame(rows, columns=columns)
    #     else:
    #         df = pd.DataFrame()
    #     return df

    # def get_table(self, table_name: str):
    #     print('model.get_table')
    #     # todo-high-prusove нужно доработать функцию, чтобы она возвращала df с chunk-ами
    #     rows = self._gateway.get_table_rows(table_name=table_name)
    #     print(rows)
    #     iterator = rows
    #     for i in iterator:
    #         print(i)
    #
    #
    #
    #     if rows is not None:
    #         columns = [column_meta[0] for column_meta in rows.description]
    #         df = pd.DataFrame(rows, columns=columns)
    #     else:
    #         df = pd.DataFrame()
    #     return df

    def get_table(self, table_name: str):
        print('отработала функция model.get_table')
        # todo-high-prusove нужно доработать функцию, чтобы она возвращала df с chunk-ами
        rows = self._gateway.get_table_rows(table_name=table_name)
        for row in rows:
            print(row)
            if row is not None:
                columns = [column_meta[0] for column_meta in row.description]
                df = pd.DataFrame(row, columns=columns)
            else:
                df = pd.DataFrame()
            yield df


    def get1000notnullrows(self, table_name: str):
        # todo-high-prusove разработать функции get1000notnullrows для Sybase IQ
        return self.get_table(table_name=table_name)
        # todo-low-prusove: научиться писать под технической учеткой в любую другую схему

    def save_table(self, table_name: str, df: pd.core.frame.DataFrame):
        return self._gateway.save_table(table_name=table_name, df = df)

    def save_table_odbc(self, table_name: str, df: pd.core.frame.DataFrame):
        return self._gateway.save_table_odbc(table_name=table_name, df=df)

class OracleDataSource(DataSource):

    def __init__(self, name, host, port, sid, user, password, table_owner):
        self.name = name
        self.host = host
        self.port = port
        self.sid = sid
        self.user = user
        self.password = password
        self.table_owner = table_owner

    def get_list_of_table_names(self):
        result = list()
        connection, cursor = create_connection(host=self.host, port=self.port, sid=self.sid, user=self.user, password=self.password)
        query_text = f"select table_name from all_tables where lower(owner) = '{self.table_owner}'"

        cursor.execute(query_text)
        # todo-medium-prusove: обработать ситуацию когда не найдено ничего
        rows = cursor.fetchall()
        if rows.__len__() != 0:
            result = [row[0] for row in rows]
        else:
            result = rows

        cursor.close()
        connection.close()

        return result

    def get_table(self, table_name: str, chunk_size=1000000):
        # conn, cursor = create_connection(host=self.host, port=self.port, sid=self.sid, user=self.user,
        #                                        password=self.password)
        conn2 = create_connection2(
            host=self.host, port=self.port, sid=self.sid, user=self.user, password=self.password)
        query_str = f'SELECT * FROM {self.table_owner}.{table_name}'
        # todo-medium-prusove: сделать свою реализацию чтения из БД и записи в df
        #df_table = pd.read_sql_query(query_str, conn2, chunksize=chunk_size)
        df_table = pd.read_sql_query(query_str, conn2)

        # cursor.close()
        # conn2.close()

        return df_table

    def get1000notnullrows(self, table_name: str):
        # todo-medium-prusove разработать функции get1000notnullrows для Oracle
        conn2 = create_connection2(
            host=self.host, port=self.port, sid=self.sid, user=self.user, password=self.password)
        query_str = f'SELECT * FROM {self.table_owner}.{table_name}'
        df_table = pd.read_sql_query(query_str, conn2)
        return df_table

    def save_table(self, table_name: str, df: pd.core.frame.DataFrame):
        # todo-medium-prusove: переписать эту дич на нормальную реализацию через cursor
        # todo-low-prusove: научиться писать под технической учеткой в любую другую схему
        conn2 = create_connection2(host='localhost', port='1521', sid='xe', user='uat_core', password='uat_core')
        df.to_sql(table_name, conn2)



class CSVDataSource(DataSource):

    def __init__(self, path):
        self.path = path

    def get_list_of_table_names(self):
        result = os.listdir(self.path)
        return result

    def get_table(self, table_name: str):
        result = pd.read_csv(os.path.join(self.path, table_name), encoding='utf8', sep=',', chunksize=1000000)
        return result

    def get1000notnullrows(self, table_name: str):
        # todo-low-aprusov разработать функции get1000notnullrows для csv
        result = pd.read_csv(os.path.join(self.path, table_name), encoding='utf8', sep=',')
        return result

    def save_table(self, table_name: str, df: pd.core.frame.DataFrame):
        df.to_csv(os.path.join(self.path, table_name), index=False)


if __name__ == '__main__':
    iq_gateway = IQGateway(host='localhost', port='2638', dbname='dwh', username='core', password='hell4min')
    ds_in = IQDataSource(name='Ядро (dev01)', gateway=iq_gateway)
