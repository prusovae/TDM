/*
truncate table client;
truncate table customer;
drop table client;
drop table customer;
*/

create table client (
    client_id integer primary key,
    fname varchar2(256),
    sname varchar2(256),
    telnum varchar2(20)
);

insert into client (client_id, fname, sname, telnum)
    VALUES (1, 'Евгений', 'Прусов', '+7(918)2495495');
insert into client (client_id, fname, sname, telnum)
    VALUES (2, 'Алексей', 'Юнов', '89161119998');
insert into client (client_id, fname, sname, telnum)
    VALUES (3, 'Андрей', 'Прусов', '8(918) 000-22-11');
insert into client (client_id, fname, sname, telnum)
    VALUES (4, 'Дмитрий', 'Тигуанов', '+79181112233');
commit;

create table customer (
    customer_id integer primary key,
    first_name varchar2(256),
    family_name varchar2(256),
    inn integer
);

insert into customer (customer_id, first_name, family_name, inn) VALUES (1000, 'Алексей', 'Юнов', 1122334455);
insert into customer (customer_id, first_name, family_name, inn) VALUES (2000, 'Евгений', 'Прусов', 9998887776);
insert into customer (customer_id, first_name, family_name, inn) VALUES (3000, 'Андрей', 'Прусов', 1010101010);
commit;
