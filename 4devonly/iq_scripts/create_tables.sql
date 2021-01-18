-- drop table d_entity;
-- drop table empty_tab;

CREATE TABLE d_entity (
    entity_id integer primary key,
    entity_type_cd varchar(5),
    birth_dt date,
    birth_place varchar(512),
    first_name varchar(128),
    second_name varchar(128),
    third_name varchar(128),
    full_name varchar(512),
    short_name varchar(128),
    tax_number varchar(32),
    code varchar(32),
    email varchar(32),
    primary_tel_nbr varchar(64),
    mobile_tel_nbr varchar(64)
);
delete from d_entity;
insert into d_entity values (1, 'PSN', '1987-11-19', 'ЦНП. йПЮЯМНДЮП', 'юкейяеи', 'яепцеебхв', 'чмнб', 'чмнб юкейяеи яепцеебхв', 'чмнб ю. я', '230815888696', 'gpbu7882', null, '', '+7(926)5375953');
insert into d_entity values (2, 'PSN', '1987-11-11', 'ЦНП. йПЮЯМНДЮП', 'ебцемхи', 'ебцемэебхв', 'опсянб', 'опсянб ебцемхи ебцемэебхв', 'опсянб е. е', '230810936191', 'gpbu8090', '', null, null);
insert into d_entity values (3, 'PSN', '1987-11-11', 'ЦНП. йПЮЯМНДЮП', 'юмдпеи', 'ебцемэебхв', 'опсянб', 'опсянб юмдпеи ебцемэебхв', 'опсянб ю. е', null, 'gpbu8704', 'ae.prusov@gmail.com', '', '+7(985)3089080');
commit;

create table empty_tab (c_id integer);

select table_name, rows_qty
  from (select 'd_entity' as table_name, count(*) as rows_qty from d_entity union all
        select 'empty_tab' as table_name, count(*) as rows_qty from empty_tab) s;