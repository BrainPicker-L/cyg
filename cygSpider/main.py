from scrapy.cmdline import execute
import os
import MySQLdb


os.chdir("/home/cyg/cygSpider")
from delete_catch import delete
delete()

conn =MySQLdb.connect("127.0.0.1", "root", "lzz804456852", "cyg_db", charset='utf8')
cursor = conn.cursor()
cursor.execute("DELETE FROM role_role")
conn.commit()
execute("scrapy crawl roleinfo".split())
#
#

conn.close()
#a = conn.execute("select * from role_role")
#for i in a:
#    print(i)
