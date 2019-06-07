import os
import MySQLdb
#os.chdir("/home/cyg/cygSpider")
conn =MySQLdb.connect("127.0.0.1", "root", "lzz804456852", "cyg", charset='utf8')
cursor = conn.cursor()
cursor.execute("""delete from role_role where id 
in (select id from (
    select id from role_role
    where (role_role.name,role_role.price) 
    in (select name,price from role_role group by name,price having count(*) > 1)
    and id not in (select min(id)  from role_role group by name,price having count(*)>1) 
)as temp );""")
conn.commit()
conn.close()