from typing import List
import sqlanydb


class SqlResult(list):
    """Когда ответ от БД не простой list, а объект, то можно добавить к нему доп. инфо,
    например добавить имена колонок из SELECT'а (делается в run_query)"""
    def __init__(self, result):
        super().__init__(result)


def connect_to_db(username, password, dbname, host, port):
    """
    Connect to IQ database and get connection and cursor.

    :param username:
    :param password:
    :param dbname:
    :param host:
    :param port:
    :param charset: Codepage setting of destination database
    :return: connection to DB, and cursor.
    """
    try:
        conn = sqlanydb.connect(uid=username, pwd=password, dbn=dbname, host=str(host) + ":" + str(port))
        curs = conn.cursor()
        print(curs)
        # logger.info(f'connection and cursor created for database {database} on host {hostname}')
        print(f'connection and cursor created for database {dbname} on host {host}')
    except Exception as e:
        # logger.error('Error while connecting to database or getting a cursor')
        print('Error while connecting to database or getting a cursor')
        raise e

    return conn, curs

def run_query_generator(cursor, query) -> None:
    cursor.execute(query)
    result = '1'
    while len(result)!=0:
        result = SqlResult(cursor.fetchmany(1000))
        result.description = cursor.description
        yield result



def run_query(cursor, query) -> None:
    """
    Run sql-based query on SAP IQ database

    :param cursor: database cursor
    :param query: sql-based query
    :param chunk: fetch limit
    :return:
    """
    try:
        # logger.info(f"executing query: {query}")
        #print(f"executing query: {query}")
        cursor.execute(query)
        result = SqlResult(cursor.fetchall())
        #result = SqlResult(cursor.fetchmany(2))
        result.description = cursor.description
        print('iq.py result = ',result)
        # logger.info(f'result is {result}')
        #print(f'result is {result}')
        #yield result if result else None
        return result if result else None
    except sqlanydb.OperationalError as er:
        # logger.exception(f'There is an error while executing query: {query}', er.message, exc_info=True)
         print(f'There is an error while executing query: {query}', er.message, exc_info=True)
    except sqlanydb.InterfaceError as er:
        if 'no result set' in er.errortext:
            # logger.debug(f'{query} is propably insert or update without an answer so passing an exception')
            #print(f'{query} is propably insert or update without an answer so passing an exception')
            pass
    except Exception as er:
        # logger.error(er.message)
        print(f'ERROR: {er.message}')
        raise er

def run_query_many(cursor, query, rows) -> None:
    cursor.autocommit = False
    cursor.fast_executemany = True
    cursor.executemany(query, rows)

    #
    # conn = pyodbc.connect(connStr, autocommit=False)
    # # conn.set_attr(pyodbc.SQL_ATTR_TXN_ISOLATION, pyodbc.SQL_TXN_SERIALIZABLE)
    # conn.autocommit = False
    # cur = conn.cursor()
    #
    # cur.fast_executemany = True
    # data = rows[total:][:chunk]
    #
    # cur.executemany(sql, data)
