
import sqlanydb
host='localhost'
port='2638'
dbname='dwh'
username='core'
password='hell4min'

conn = sqlanydb.connect(uid=username, pwd=password, dbn=dbname, host=str(host) + ":" + str(port))


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
        # logger.info(f'connection and cursor created for database {database} on host {hostname}')
        print(f'connection and cursor created for database {dbname} on host {host}')
    except Exception as e:
        # logger.error('Error while connecting to database or getting a cursor')
        print('Error while connecting to database or getting a cursor')
        raise e

    return conn, curs


def run_query(cursor, query) -> None:
    """
    Run sql-based query on SAP IQ database

    :param cursor: database cursor
    :param query: sql-based query
    :return:
    """
    try:
        # logger.info(f"executing query: {query}")
        print(f"executing query: {query}")
        cursor.execute(query)
        result = SqlResult(cursor.fetchall())
        result.description = cursor.description

        # logger.info(f'result is {result}')
        # print(f'result is {result}')
        return result if result else None
    except sqlanydb.OperationalError as er:
        # logger.exception(f'There is an error while executing query: {query}', er.message, exc_info=True)
        print(f'There is an error while executing query: {query}', er.message, exc_info=True)
    except sqlanydb.InterfaceError as er:
        if 'no result set' in er.errortext:
            # logger.debug(f'{query} is propably insert or update without an answer so passing an exception')
            print(f'{query} is propably insert or update without an answer so passing an exception')
            pass
    except Exception as er:
        # logger.error(er.message)
        print(f'ERROR: {er.message}')
        raise er