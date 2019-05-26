import os
import shutil
import re
def delete():
    dir = "/home/cyg/cygSpider/.scrapy/httpcache/roleinfo"
    for root, dirs, files in os.walk(dir):
        #print(root)
        for file in files:
            if file == "meta":
                f = open(root+"/"+file)
                text = f.read()
                if 'page_num=' in text:
                    page_num = int(re.findall(r'page_num=(\d+)',text)[0])
                    if page_num<=20:
                        root_delete = root
                        f.close()
                        shutil.rmtree(root_delete)


if __name__ == "__main__":
    delete()
