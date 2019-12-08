from scrapy.cmdline import execute
import os
import MySQLdb


os.chdir("/home/cyg/cygSpider")
from conf import HOST,PORT,USER,PASSWORD,DB_NAME
from delete_catch import delete
delete()

conn =MySQLdb.connect(HOST, USER, PASSWORD, DB_NAME, charset='utf8')
cursor = conn.cursor()
cursor.execute("DELETE FROM role_role")
conn.commit()
execute("scrapy crawl roleinfo".split())
cursor.execute("""delete from role_role where id
in (select id from (
    select id from role_role
    where (role_role.name,role_role.attack_heightest_value)
    in (select name,attack_heightest_value from role_role group by name,attack_heightest_value having count(*) > 1)
    and id not in (select min(id)  from role_role group by name,attack_heightest_value having count(*)>1)
)as temp );""")
conn.commit()
conn.close()

