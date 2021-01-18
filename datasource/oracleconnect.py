# import cx_Oracle
# from sqlalchemy import types, create_engine
# def create_connection(host: str, port: str, sid: str, user: str, password: str):
#     conn_str = f'{user}/{password}@{host}:{port}/{sid}'
#     connection = cx_Oracle.connect(conn_str, encoding="UTF-8")
#     cursor = connection.cursor()
#     return connection, cursor
#
#
# if __name__ == '__main__':
#     #connection, cursor = create_connection(host='localhost', port='1251', sid='XE', user='core', password='core')
#     connection, cursor = create_connection(host='localhost', port='1521', sid='XE', user='core', password='core')
#
#     cursor.execute("select table_name from all_tables where owner = 'SYS'")
#
#     result = cursor.fetchall()
#     print(result)



#columns1 = Index(['crm_client_id', 'name', 'midname', 'surname', 'email', 'mobile_num','fio', 'card_num', 'inn', 'comments'],dtype='object')
columns = ['crm_client_id', 'name', 'midname', 'surname', 'email', 'mobile_num', 'fio', 'card_num', 'inn', 'comments']



column = ""
for i in columns:
    column+=i+','
column = (column[:-1])
print(column)