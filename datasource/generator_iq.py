import sqlanydb
con = sqlanydb.connect( userid='dba', pwd='hell4min', servername='iqserver', host='localhost:2638' )
cursor = con.cursor()
sql = 'SELECT * from core.crm_client'

cursor.execute(sql)
set_count = 0
#result = cursor.fetchone()
# def mygenerator():
#     result = cursor.fetchmany(2)
#     yield result
# #
# myiterator = mygenerator()
# #print(result)
# def chunk():
#     myiterator = mygenerator()
#     result = [i for i in myiterator]
#     return result
#
#

result = '1'
while len(result) !=0:
    result = cursor.fetchmany(150)
    print(result, end='\n')
    set_count+=1
    print('Прочитано сетов - ',set_count)
