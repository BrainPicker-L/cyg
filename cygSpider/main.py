from scrapy.cmdline import execute
import os
import sqlite3
<<<<<<< HEAD
conn =sqlite3.connect("../db.sqlite3", isolation_level=None)
=======
os.chdir("/home/cyg/cygSpider")
from delete_catch import delete
delete()
conn =sqlite3.connect("/home/cyg/db.sqlite3", isolation_level=None)
>>>>>>> 08ac268658e87391da30352670ad9f02af7b03de
conn.execute("DELETE FROM role_role")
execute("scrapy crawl roleinfo".split())
#
#
conn.execute("delete from role_role where role_role.rowid not in (select MAX(role_role.rowid) from role_role group by detail_url)")
conn.execute('vacuum')
conn.close()
#a = conn.execute("select * from role_role")
#for i in a:
#    print(i)