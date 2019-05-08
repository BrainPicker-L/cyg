import requests
from lxml import etree
import re
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.81 Safari/537.36'
}
html = requests.get("http://tl.cyg.changyou.com/goods/char_detail?serial_num=201903011822187967",headers=headers).text

a = re.findall('sd r">\d*',html)
b = []
for i in a:
    b.append(int(i.split(">")[1]))
print(max(b))



# a = re.findall("融合度.*</span>",html)
# b = re.findall("悟性.*</i>",html)
# c = re.findall("灵性.*</i>",html)=
#
# for i in range(len(a)):
#     try:
#         ronghe = re.findall('\d\d',a[i])[0]
#         if ronghe != "10":
#             continue
#         wuxing = re.findall('\d\d',b[i])[0]
#         if wuxing != "10":
#             continue
#         lingxing = re.findall('\d\d',c[i])[0]
#         if lingxing != "10":
#             continue
#
#         if ronghe==wuxing==lingxing=="10":
#             print("有30")
#     except:
#         pass