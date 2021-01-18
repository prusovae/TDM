Для работы с IQ нужно:
1) скачать и установить SAP IQ Express Edition
   download link: https://1drv.ms/u/s!AmjTOfENFYENgrxqXenFQ2Z7oglu7A?e=GrN2pB
2) скачать и установить клиент SQL Anywhere
   download link: https://1drv.ms/u/s!AmjTOfENFYENgrxo48CCq2i8adhXow?e=wIONLV
3) создать новую БД (кодировка win1251)
   а) Создать БД
      iqinit -iqpath dwh.iq -iqsize 4096M dwh.db -dba DBA,hell4min -z 1251CYR
      # где логин:DBA, пароль:hell4min
   б) Запустить БД
      iqsrv16 -n iqserver -iqlm 8096 -iqtc 2048 c:\ProgramData\SAPIQ\dwh\dwh.db

 - настроить подключение
   а) в pycharm подключить jdbc драйвер: c:\iqclient\IQ-16_1\Java\sajdbc.jar
    ,где путь к jdbc это путь к клиенту SQL Anywhere из п.2
   б) пример url: jdbc:sqlanywhere:UserID=dba;Password=hell4min;Host=localhost:2638;ServerName=iqserver;DatabaseName=dwh;
     , где ServerName - задается при старте БД, DatabaseName - задается при создании БД (у меня это dwh)

В win10 по умолчанию стоит кодировка win1251 и явно ее в connect_string прописывать не нужно
Чтобы проверить что кодировки сервера, клиента и БД одинаковые (win1251), выполните запросы:
- SELECT PROPERTY('CharSet');
- SELECT DB_PROPERTY('CharSet');
- SELECT CONNECTION_PROPERTY('CharSet'); -- задать в connect_string
DB_PROPERTY и CONNECTION_PROPERTY должны выдавать win1251.

ВАЖНО: файлы sql с insert'ами тестовых данных нужно сохранять в кодировке win1251.
Чтобы это сделать, нужно зайти в File -> Settings -> Editor -> File Encodings и
выбрать для соотв. файлов кодировки win1251, т.к. по умолчанию в проекте все в utf-8.