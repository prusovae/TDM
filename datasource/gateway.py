from typing import List
from datasource.iq import connect_to_db, run_query, run_query_many, run_query_generator
import csv
import pandas as pd
#import time
from datasource.pyodbc_iq import run_query_odbc_many

import memory_profiler
import copy

class IQGateway:

    def __init__(self, host, port, dbname, username, password):
        self.host = host
        self.port = port
        self.dbname = dbname
        self.username = username
        self.password = password
        self._conn, self._curs = connect_to_db(
            username=self.username, password=self.password, dbname=self.dbname, host=self.host, port=self.port)

    def get_list_of_table_names(self) -> List[str]:
        # TODO: Нужно добавить фильтр на BASE TABLE
        sql_text = f"""select t.table_name
                           from sysuser u
                           join systab t on t.creator = u.user_id
                          where u.user_name = '{self.username}'
                          -- and t.table_name = 'test_not_null'
                          order by t.table_name;"""
        sql_response = run_query(self._curs, sql_text)
        table_names = [x[0] for x in sql_response] if sql_response is not None else list()
        return table_names

    # def get_table_rows(self, table_name: str):
    #     rows = run_query(self._curs, f'select * from {self.username}.{table_name};')
    #     print('gateway rows = ',rows)
    #     return rows
    def get_table_rows(self, table_name: str):
        rows = run_query_generator(self._curs, f'select * from {self.username}.{table_name};')
        #print('Переменной gateway.rows присвоено значение - ',rows)
        return rows

    def save_table(self, table_name: str, df : str):
        print('table - ',table_name)
    #     df = df.applymap(str)
    #     rows = df.values.tolist()
    #     parms = ("?," * len(rows[0]))[:-1]
    #     sql = f"INSERT INTO {self.username}.{table_name} VALUES (%s)" % (parms)
    #     result = run_query_many(self._curs, sql, rows)
    #
    #     self._conn.commit()
    #     return result

    # Текущий загрузчик через файлы
    #     print(df)
    #     print(df.values)
        column = ""
        for i in df.columns:
            #print(i)
            column += i + ','
        column = (column[:-1])

        df.to_csv(f'C:\\dataset\\{self.username}.{table_name}.txt', header=None, index=None, sep='|', mode='w', line_terminator='\n', na_rep = '')
        sql_text = f"LOAD TABLE {self.username}.{table_name}({column}) using client file 'C:\\dataset\\{self.username}.{table_name}.txt' FORMAT BCP escapes off quotes on delimited by '|' ROW DELIMITED BY '\\n';"
        # sql_text_ =f"LOAD TABLE {self.username}.{table_name}({column}) using client file 'C:\\dataset\\{self.username}.{table_name}.txt' FORMAT BCP escapes off delimited by '|' ROW DELIMITED BY '\\n';"
        result = run_query(self._curs, sql_text)
        self._conn.commit()
        return result




    # def save_table_odbc(self, table_name: str, df: str):
        # df = df.applymap(str)
        # rows = df.values.tolist()
        # parms = ("?," * len(rows[0]))[:-1]
        # sql = f"INSERT INTO {self.username}.{table_name} VALUES (%s)" % (parms)
        # result = run_query_odbc_many(self._curs, sql, rows)
        #
        # self._conn.commit()
        # return result







        # Запись маскированной таблицы в файл
        # column = ""
        # for i in df.columns:
        #     column += i + ','
        # column = (column[:-1])
        #
        # df.to_csv(f'{self.username}.{table_name}.txt', header=None, index=None, sep='|', mode='w', line_terminator='\n')
        # sql_text =f"LOAD TABLE {self.username}.{table_name}({column}) using client file 'C:\\dataset\\{self.username}.{table_name}.txt' FORMAT BCP escapes off delimited by '|' ROW DELIMITED BY '\\n';"
        # #sql_text_ =f"LOAD TABLE {self.username}.{table_name}({column}) using client file 'C:\\dataset\\{self.username}.{table_name}.txt' FORMAT BCP escapes off delimited by '|' ROW DELIMITED BY '\\n';"
        # result = run_query(self._curs, sql_text)
        # self._conn.commit()
        # return result

        # print(sql_text)

        #LOAD TABLE uat_core.client5(crm_client_id, name, midname, surname, email, mobile_num, fio, card_num, inn, comments) using client file 'C:\dataset\uat_core.client5.txt' FORMAT BCP escapes off delimited by '|' ROW DELIMITED BY '\n';
        # Генерация insert из df
        # pd.set_option("display.max_colwidth", 350)
        # df['insert'] = f"insert into {self.username}.{table_name} values('" + df['crm_client_id'].astype('str') + "', '" + \
        #                df['name'] + "', '" + df['midname'] + "', '" + df['surname'] + "', '" + \
        #                df['email'] + "', '" + df['mobile_num'].astype('str') + "', '" + df['fio'] + "', '" + df[
        #                    'card_num'].astype('str') + "', '" + df['inn'].astype('str') + "', '" + df['comments'] + "');"
        # sql_text = df['insert']
        # sql_text = sql_text.to_string(index=False)
        # sql_text = " ".join([el for el in sql_text.split(' ') if el.strip()])
        # result = run_query(self._curs, sql_text)
        # self._conn.commit()
        # return result


        # sql_text = ''
        # k = 0
        # s = 0
        # for i in df.values.tolist():
        #     k += 1
        #     sql = f"insert into {self.username}.{table_name} values('" + "','".join([str(j) for j in i]) + "');"
        #     sql_text = sql_text + sql + "\n"
        #     s+=1
        #     print(k)
        #     if s ==5000:
        #         s=0
        #         result = run_query(self._curs, sql_text)
        #     self._conn.commit()

        # sql_text = ''
        # k = 0
        # s = 0
        # for i in df.values.tolist():
        #     k += 1
        #     sql = f"insert into {self.username}.{table_name} values('" + "','".join([str(j) for j in i]) + "');"
        #     sql_text = sql_text + sql + "\n"
        #     s += 1
        #
        #     if s == 1000:
        #         print(k,'rows commit to table ', table_name)
        #         s = 0
        #         result = run_query(self._curs, sql_text)
        #         sql_text = ''
        #     self._conn.commit()


        # insert as select
        # sql_text = f"create table {self.username}.{table_name}_test_speed as (select * from core.{table_name});"
        # result = run_query(self._curs, sql_text)
        # self._conn.commit()
        # return result
