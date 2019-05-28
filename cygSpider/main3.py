
import os
import sqlite3
os.chdir("/home/cyg/cygSpider")
conn =sqlite3.connect("/home/cyg/db.sqlite3", isolation_level=None)
conn.execute("delete from role_role where role_role.rowid not in (select MAX(role_role.rowid) from role_role group by detail_url)")
conn.execute('vacuum')
conn.close()
