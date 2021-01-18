import pyodbc
pyodbc.drivers()
conn = pyodbc.connect(driver='Sybase IQ', server='iqserver', port='2638', database='dwh', uid='uat_core', pwd='hell4min')
cursor = conn.cursor()


def run_query_odbc_many(cursor, query, rows) -> None:
    cursor.autocommit = False
    print('cursor.fast_executemany = True')
    cursor.fast_executemany = True
    print(cursor.fast_executemany)
    cursor.executemany(query, rows)