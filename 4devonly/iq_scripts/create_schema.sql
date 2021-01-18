CREATE USER core identified by Ab123456;
ALTER USER core identified by 'Ab123456';
GRANT CONNECT to core;
GRANT RESOURCE to core;

CREATE USER uat_core;
ALTER USER uat_core identified by 'Ab123456';
GRANT CONNECT to uat_core;
GRANT RESOURCE to uat_core;

select * from sysuser where user_name like '%core';