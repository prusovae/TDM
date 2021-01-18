import cx_Oracle
from sqlalchemy import types, create_engine


def create_connection2(host: str, port: str, sid: str, user: str, password: str):
    conn = create_engine(
        f'oracle+cx_oracle://{user}:{password}@{host}:{port}/?service_name={sid}',max_identifier_length=128,
        connect_args={"encoding": "UTF-16",}
    )
    return conn


def create_connection(host: str, port: str, sid: str, user: str, password: str):
    conn_str = f'{user}/{password}@{host}:{port}/{sid}'
    connection = cx_Oracle.connect(conn_str, encoding="UTF-8")
    cursor = connection.cursor()
    return connection, cursor

def run_query_many(cursor, query, rows) -> None:
    cursor.executemany(query, rows)

if __name__ == '__main__':
    connection, cursor = create_connection(host='localhost', port='1521', sid='xe', user='core', password='core')


    cursor.execute("select table_name from all_tables where owner = 'SYS'")

    result = cursor.fetchall()
    print(result)