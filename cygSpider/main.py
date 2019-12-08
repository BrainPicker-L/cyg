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

conn.close()

