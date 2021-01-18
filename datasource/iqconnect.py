import pandas as pd
from pandas import DataFrame
import sqlanydb
con = sqlanydb.connect( userid='dba', pwd='hell4min', servername='iqserver', host='localhost:2638' )
cursor = con.cursor()
select_query = 'SELECT * from core.crm_client'

crm_client = {'crm_client_id':['1','2','3','4'],
              'name': ['Серик', None, 'Семен', 'Асланбек'],
              'midname': ['sdf', 'sdfs', 'gdsd', 'kj'],
              'surname': ['sdf', 'fgfd', 'rfv', 'tyh'],
              'email': ['e', 'w', 'r', 't'],
              'mobile_num': [3, 4, 5, 6],
              'fio': ['a', 'f', 'k', 'g'],
              'card_num': [2345, 542, 3456, 745],
              'inn': [76, 56, 54, 34],
              'comments':['f', 'd', 'e', 'f']
              }
df = DataFrame(crm_client, columns= ['crm_client_id', 'name', 'midname','surname','email','mobile_num','fio','card_num','inn','comments'])
#print(df)
print(df.info())
df = df.applymap(str)
print(df.info())
# val = df.values.tolist()
#print(val)

# stmt2 = "insert into testy (v1) values (?)"
# list_of_lists = [[list1], [list2], [list3]]
# cs.executemany(stmt2, list_of_lists)
#
#[print(str(i)) for i in range(500000)]
#val = [str(i) for i in range(100000)]
#val = [["1","2"],["2","3"]]
#cursor.executemany('insert into uat_core.crm_client values(?,?,?,?,?,?,?,?,?,?)', val)
#cursor.executemany('insert into uat_core.crm_client values(?)', val)
#print("complete")

# Пример
# rows = ((801,'Alex','Alt','5 Blue Ave','New York','NY',
#         'USA','10012','5185553434','BXM'),
#         (802,'Zach','Zed','82 Fair St','New York','NY',
#         'USA','10033','5185552234','Zap'))

#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# Set up a parameterized SQL INSERT
#rows = df.values.tolist()
rows = [['1', 'Серик', 'sdf', 'sdf', 'e', '3', 'a', '2345', '76', 'f'], ['2', None, 'sdfs', 'fgfd', 'w', '4', 'f', '542', '56', 'd'], ['3', 'Семен', 'gdsd', 'rfv', 'r', '5', 'k', '3456', '54', 'e'], ['4', 'Асланбек', 'kj', 'tyh', 't', '6', 'g', '745', '34', 'f']]
#parms = ("?," * len(rows[0]))[:-1]
sql = "INSERT INTO uat_core.crm_client VALUES (%s)" % (("?," * len(rows[0]))[:-1])
print(sql)
print(rows)
cursor.executemany(sql, rows)
cursor.close()
con.commit()
con.close()
# cur.execute("insert into atable (name, ctime) values (%s, %s)", ('aname', None))

# variable = 'NULL'
# insert_query = """insert into my_table values(date'{}',{},{})"""
# format_query = insert_query.format('9999-12-31', variable, variable)
# curr.execute(format_query)
# conn.commit()
#
# >> insert into my_table values(date'9999-12-31',NULL,NULL)


# cursor.executemany("insert into uat_core.crm_client(crm_client_id, name, midname,surname,email,mobile_num,fio,card_num,inn,comments) values (?);", a)
# #cursor.executemany("insert into uat_core.crm_client values (?);", a)
#con.commit()


# DATABASE_CHUNK_SIZE = 50000
#
# for group in grouper(db_rows, DATABASE_CHUNK_SIZE):
#     cursor.executemany(
#         "INSERT INTO yourtable (col1, col2, col3) VALUES (%s, %s, %s);",
#         [x for x in group if x is not None]
#     )


# def test_executemany(self):
#     con = self._connect()
#     try:
#         cur = con.cursor()
#         self.executeDDL1(cur)
#         largs = [("Cooper's",), ("Boag's",)]
#         margs = [{'beer': "Cooper's"}, {'beer': "Boag's"}]
#         if self.driver.paramstyle == 'qmark':
#             cur.executemany(
#                 'insert into %sbooze values (?)' % self.table_prefix,
#                 largs
#             )
#         elif self.driver.paramstyle == 'numeric':
#             cur.executemany(
#                 'insert into %sbooze values (:1)' % self.table_prefix,
#                 largs
#             )
#         elif self.driver.paramstyle == 'named':
#             cur.executemany(
#                 'insert into %sbooze values (:beer)' % self.table_prefix,
#                 margs
#             )
#         elif self.driver.paramstyle == 'format':
#             cur.executemany(
#                 'insert into %sbooze values (%%s)' % self.table_prefix,
#                 largs
#             )
#         elif self.driver.paramstyle == 'pyformat':
#             cur.executemany(
#                 'insert into %sbooze values (%%(beer)s)' % (
#                     self.table_prefix
#                 ),
#                 margs
#             )





# Обратите внимание, даже передавая одно значение - его нужно передавать кортежем!
# Именно по этому тут используется запятая в скобках!
# new_artists = [('A Aagrh!',),
#                ('A Aagrh!-2',),
#                ('A Aagrh!-3',),]
# cursor.executemany("insert into Artist values (Null, ?);", new_artists)






# KiB = 1024
# MiB = 1024 * KiB
# GiB = 1024 * MiB
#
# with open('/proc/meminfo') as f:
#     ram = f.readline()
#     ram = ram[ram.index(' '):ram.rindex(' ')].strip()
#     ram = int(ram) * KiB / GiB
#
# required = sys.getsizeof(42) * 1_000_000_000 / GiB
#
# print('Надо:', required, 'GiB')
# print('Есть:', ram, 'GiB')
#
# if required > ram:
#     print('У тебя совесть есть, сцуко?!')



#
# cursor.execute(select_query)
# result = cursor.fetchall()
# cursor.close()
# # print('result',result)
# df = DataFrame(result)
# print(df)#
# print(df.columns)
# k=0
# s=0
# sql_text=''
# for i in df.values.tolist():
#     k+=1
#     sql = "insert into uat_core.crm_client values('" + "','".join([str(j) for j in i])+"');"
#     # print(sql)
#     print(k)
#     #sql_text = sql_text + '\n' + sql
#
#
#
#
# print('all',sql_text)

# print(df.columns)
#
#
# pd.set_option("display.max_colwidth", 350)
# df['insert'] = "insert into uat_core.crm_client values('" + df['crm_client_id'].astype('str') + "', '" + df['name'] + "', '" + df['midname'] + "', '" + df['surname'] + "', '" + df['email'] + "', '" + df['mobile_num'].astype('str') + "', '" + df['fio'] + "', '" + df['card_num'].astype('str') + "', '" + df['inn'].astype('str') + "', '" + df['comments'] + "');"
# sql_text = df['insert']
# sql_text = sql_text.to_string(index=False)
# sql_text = " ".join([el for el in sql_text.split(' ') if el.strip()])
# print(sql_text)



# set_count = 0
#
# def mygenerator():
#     result = cursor.fetchmany(10)
#     yield result
#
#
# myiterator = mygenerator()
# myiterator
# print(myiterator)
# for i in myiterator:
#     print(i)
#
# myiterator = mygenerator()
# myiterator
# print(myiterator)
# for i in myiterator:
#     print(i)
# # while len(result) !=0:
# #     result = cursor.fetchmany(40000)
# #     print(result, end='\n')
# #     set_count+=1
# # print('Прочитано сетов - ',set_count)
# # cursor.close()
# # mylist = [1]
# # if len(mylist) != 0:
# #     print('not None')
# # else:
# #     print('is None')


####
# crm_client = {'crm_client_id':[1,2,3,4],
#               'name': ['Серик', 'Аветик', 'Семен', 'Асланбек'],
#               'midname': ['sdf', 'sdfs', 'gdsd', 'kj'],
#               'surname': ['sdf', 'fgfd', 'rfv', 'tyh'],
#               'email': ['e', 'w', 'r', 't'],
#               'mobile_num': [3, 4, 5, 6],
#               'fio': ['a', 'f', 'k', 'g'],
#               'card_num': [2345, 542, 3456, 745],
#               'inn': [76, 56, 54, 34],
#               'comments':['f', 'd', 'e', 'f']
#               }
# df = DataFrame(crm_client, columns= ['crm_client_id', 'name', 'midname','surname','email','mobile_num','fio','card_num','inn','comments'])
# df1 = DataFrame(crm_client, columns= ['crm_client_id', 'name', 'midname','surname','email','mobile_num','fio','card_num','inn','comments'])
# pd.set_option("display.max_colwidth", 350)
#df['insert'] = f"insert into core.crm_client values('" + df['crm_client_id'].astype('str') + "', '" + df['name'] + "', '" + df['midname'] + "', '" + df['surname'] + "', '" + df['email'] + "', '" + df['mobile_num'].astype('str') + "', '" + df['fio'] + "', '" + df['card_num'].astype('str') + "', '" + df['inn'].astype('str') + "', '" + df['comments'] + "');"
#sql_text = df['insert']
#print(sql_text)
# a = df['name']
# print(a)
# c =  f"df['"+"'].astype('str') + \" \" +  df['".join([str(i) for i in df1.columns])+"']"
# print(c)

# df['insert'] = a
# print(df['insert'])

#a = [i for i in df.columns]
#print(a)

# #b = '"insert into core.crm_client values("'+["df['"+i+"'].astype('str') + ', '" for i in df.columns]
#b = "insert into core.crm_client values(['"+"'].astype('str') + ', ' + df['".join([str(i) for i in df1.columns])+"]);"
# b = "insert into uat_core.crm_client values('\" + df['"+"'].astype('str') + \"', '\" + df['".join([str(i) for i in df1.columns])+"'); + \"');\""
# #print(b)
# c =  "df1['"+"'].astype('str') + \" \" +  df1['".join([str(i) for i in df1.columns])+"']"
# df['insert'] =  df['crm_client_id'].astype('str') + " " + df['name'] + " " + df['midname'] + " " + df['surname'] + " " + df['email'] + " " + df['mobile_num'].astype('str') + " " + df['fio'] + " " + df['card_num'].astype('str') + " " + df['inn'].astype('str') + " " + df['comments']
# df1['insert'] = print(c) #= df1['crm_client_id'].astype('str') + " " +  df1['name'].astype('str') + " " +  df1['midname'].astype('str') + " " +  df1['surname'].astype('str') + " " +  df1['email'].astype('str') + " " +  df1['mobile_num'].astype('str') + " " +  df1['fio'].astype('str') + " " +  df1['card_num'].astype('str') + " " +  df1['inn'].astype('str') + " " +  df1['comments']
# print(df['insert'])
# print(df1['insert'])


#df1['insert'] = "df1['"+"'] + \" \" +  df1['".join([str(i) for i in df1.columns])+"']"
#df1['insert'] = c
#print(c)
# #df['insert'] = f"insert into core.crm_client values(['"+"'].astype('str') + ', ' + df['".join([str(i) for i in df.values])+"]);"
# df['insert'] = f"insert into core.crm_client values('"+"'".join([str(i) for i in df.values])+"]);"
# sql_text = df['insert']
# print(sql_text)


#pd.set_option("display.max_colwidth", 440)

#df['insert'] =  "insert into uat_core.crm_client values('" + df['crm_client_id'].astype('str') + "', '" + df['name'] + "', '" + df['midname'] + "', '" + df['surname'] + "', '" + df['email'] + "', '" + df['mobile_num'].astype('str') + "', '" + df['fio'] + "', '" + df['card_num'].astype('str') + "', '" + df['inn'].astype('str') + "', '" + df['comments'] + "');"
#df['insert'] =  df['crm_client_id'].astype('str') + " " + df['name'] + " " + df['midname'] + " " + df['surname'] + " " + df['email'] + " " + df['mobile_num'].astype('str') + " " + df['fio'] + " " + df['card_num'].astype('str') + " " + df['inn'].astype('str') + " " + df['comments']
               # insert into uat_core.crm_client values('" + df['crm_client_id'].astype('str') + "', '" + df['name'].astype('str') + "', '" + df['midname'].astype('str') + "', '" + df['surname'].astype('str') + "', '" + df['email'].astype('str') + "', '" + df['mobile_num'].astype('str') + "', '" + df['fio'].astype('str') + "', '" + df['card_num'].astype('str') + "', '" + df['inn'].astype('str') + "', '" + df['comments]);
#df1['insert'] = "insert into uat_core.crm_client values('\" + df['"+"'].astype('str') + \"', '\" + df['".join([str(i) for i in df1.columns])+"'); + \"');\""
#df1['insert'] = b
#print(df['insert'])
#print(df1['insert'])


#df['insert'] = b
# sql_text = df['insert']
# print(df['insert'])
#
# print(b)
# #print(sql_text)
# sql_text = sql_text.to_string(index=False)
# sql_text = " ".join([el for el in sql_text.split(' ') if el.strip()])
# print(sql_text)



# print(df)
# #print(df.values.tolist())
# all_sql = ''
# for i in df.values.tolist():
#     sql = "insert into uat_core.crm_client values('" + "','".join([str(j) for j in i])+"');"
#
#     all_sql=all_sql+'\n'+sql
#     #print("insert into uat_core.crm_client values('" + "','".join([str(j) for j in i])+"');")
#     #cursor.execute(sql)
# print('sql',all_sql)
# # creating column list for insertion
# #cols = "`,`".join([str(i) for i in df.columns.tolist()])
#
# # Insert DataFrame recrds one by one.
# #for row in df.iteritems():
#     #print("INSERT INTO `uat_core.crm_client` (`" + cols + "`) VALUES ("+str(df.values[0])+")")
#     #sql = "INSERT INTO `uat_core.crm_client` (`" +cols + "`) VALUES (" + "%s,"*(len(row)-1) + "%s)"
#     #cursor.execute(sql, tuple(row))
#     #
#     # # the connection is not autocommitted by default, so we must commit to save our changes
#     # con.commit()













# Execute a SQL string
#sql = "SELECT * FROM core.crm_client"
# cursor.execute(sql)
# cursor.commit


#
# rowset = cursor.fetchall()
# for row in rowset:
#     print(row)
# cursor.close()
# con.close()

# list of strings


#
# 2,'Алексей','Сергеевич', 'Юнов',    'yunov@lolkek.ru',     '89161119998', 'Юнов Алексей СЕРГЕЕВИЧ',      '230810936017', '4249170002067101', 'отправил вместе с юновым 100 руб.');
# 3,'Андрей', 'Евгеньевич','Прусов',  'elfwinobuf@yandex.ru','89853089080',' ПРУСОВ  АНДРЕЙ ЕВГЕНЬЕВИЧ',   '23081093601', '4249170002067102','');
# 4,'Дмитрий','Матрасович','Тигуанов','dimyan@orehov.com',   '89181112233',' Тигуанов ДМИТРИЙ матрасович', '2308109360155', '4249170002067103','');
#
#
# # Create DataFrame
# df = pd.DataFrame(data)
#
# # Print the output.
# print(df)
# print(df['name'][0],df['inn'][0])

