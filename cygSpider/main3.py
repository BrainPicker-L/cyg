import os
import MySQLdb
#os.chdir("/home/cyg/cygSpider")
conn =MySQLdb.connect("127.0.0.1", "root", "lzz804456852", "cyg_db", charset='utf8')
cursor = conn.cursor()
cursor.execute("""delete from role_role where id 
in (select id from (
    select id from role_role
    where (role_role.name,role_role.attack_heightest_value) 
    in (select name,attack_heightest_value from role_role group by name,attack_heightest_value having count(*) > 1)
    and id not in (select min(id)  from role_role group by name,attack_heightest_value having count(*)>1) 
)as temp );""")
conn.commit()
conn.close()
