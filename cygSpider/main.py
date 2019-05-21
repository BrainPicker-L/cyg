from scrapy.cmdline import execute
import os
import sqlite3
import sys
# print(os.path.abspath(os.path.dirname(__file__)))
# execute("scrapy crawl roleinfo".split())

conn =sqlite3.connect("../db.sqlite3", isolation_level=None)
#conn.execute("delete from role_role where role_role.rowid not in (select MAX(role_role.rowid) from role_role group by detail_url)")
#conn.execute('vacuum')
cursor = conn.execute("SELECT * from role_role Where menpai='少林'")
for i in cursor:
    print(i)