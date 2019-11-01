from scrapy.cmdline import execute
import os
os.chdir("/home/cyg/cygSpider")
from delete_catch2 import delete
delete()
execute("scrapy crawl roleinfo".split())

