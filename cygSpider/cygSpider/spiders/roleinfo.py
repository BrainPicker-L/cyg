# -*- coding: utf-8 -*-
import scrapy
from cygSpider.items import RoleItem
import re
import time
from role.models import *
# conda activate cyg_py36
# python manage.py runserver
# scrapy crawl roleinfo
import json
class RoleinfoSpider(scrapy.Spider):
    name = 'roleinfo'
    allowed_domains = ['changyou.com']
    start_urls = []
    for start_url in ["public", "selling"]:
        start_urls.append('http://tl.cyg.changyou.com/goods/{}?gem_level=5&gem_num=30&order_by=baoshi-desc&price=10-9999&have_chosen=gem_level*5%20price*10-9999'.format(start_url))
    def parse(self, response):
        li_list = response.xpath("//ul[@class='pg-goods-list']/li")
        hours_now = int(time.strftime('%H',time.localtime(time.time())))
        # if hours_now in [i for i in range(8,25)]:
        #     for li in li_list:
        #         item = RoleItem()
        #         item['price'] = int((li.xpath("./div/p[@class='price']/text()").extract_first())[1:])
        #         item['detail_url'] = li.xpath("./span[@class='item-img']/a/@href").extract_first()
        #         yield scrapy.Request(
        #             item['detail_url'],
        #             callback=self.parse_detail,
        #             meta={"item":item},
        #             dont_filter=False
        #         )
        #     #翻页
        #     next_url = response.xpath("//div[@class='ui-pagination']/a[@class='after']/@href").extract_first()
        #     page_num = int(re.findall(r'page_num=(\d+)',next_url)[0])
        #     if next_url != '' and page_num<=20:
        #         yield scrapy.Request(
        #             next_url,
        #             callback=self.parse,
        #             dont_filter=False
        #         )
        # else:
        for li in li_list:
            item = RoleItem()
            item['price'] = int((li.xpath("./div/p[@class='price']/text()").extract_first())[1:])
            item['detail_url'] = li.xpath("./span[@class='item-img']/a/@href").extract_first()
            yield scrapy.Request(
                item['detail_url'],
                callback=self.parse_detail,
                meta={"item":item},
                dont_filter=False
            )
        #翻页
        next_url = response.xpath("//div[@class='ui-pagination']/a[@class='after']/@href").extract_first()
        #page_num = int(re.findall(r'page_num=(\d+)',next_url)[0])
        if next_url != '':
            yield scrapy.Request(
                next_url,
                callback=self.parse,
                dont_filter=False
            )


    def parse_detail(self, response):   #处理详情页
        item = response.meta["item"]
        html = response.body.decode('utf-8')


        # 移骨丹判断
        yigudan = re.findall(r'移骨丹', html)
        if len(yigudan) != 0:
            item["yigudan"] = 1

        #  强力珍兽数量计算 成长率+最高资质>= 7000
        zizhi_list = [int(i) for i in re.findall(r'资质：\S*?span.*?>(\d+)', html)]
        growrate_list = re.findall(r'成长率：<br>.*growRate="(\d+)"', html)
        item["nb_animal_num"] = 0
        for i in range(0, len(zizhi_list), 5):
            try:
                biggest_zizhi = max(zizhi_list[i:i+5][:2])
                growrate = int(growrate_list[int(i/5)])
                if biggest_zizhi + growrate >=7000:
                    item["nb_animal_num"] += 1
            except:
                pass




        wuxing = re.findall('悟性：<i>(\d+)',html)
        lingxing = re.findall('灵性：<i>(\d+)',html)
        ronghedu = re.findall('融合度：<span class="span">(\d+)',html)
        item["if30"] = 0
        for i in range(len(wuxing)):
            if wuxing[i] == lingxing[i] == ronghedu[i] == "10":
                item["if30"] = 1
                break
        #判断双10
        item["if20"] = 0
        for i in range(len(wuxing)):
            if wuxing[i] == lingxing[i] == "10" and ronghedu[i] != "10":
                item["if20"]+=1
            else:
                pass

        #拿到武魂成长率
        item["wuhun"] = re.findall('<p>成长率：<i class="g">.{2}(\d+)</i></p>', html)
        if item["wuhun"] == []:
            item["wuhun"] = 0
        else:
            item["wuhun"] = int(item["wuhun"][0])

        #三级材料数量统计
        mianbu = re.findall(r'"3级棉布","icon":"Ore_14","typeDesc":"特殊材料","num":(\d+)', html)
        miyin = re.findall(r'"name":"3级秘银","icon":"Ore_13","typeDesc":"特殊材料","num":(\d+)', html)
        mianbu = sum(list(map(int, mianbu)))
        miyin = sum(list(map(int, miyin)))
        item["cailiao_3"] = mianbu + miyin


        #时装数量统计
        item['shizhuang_num'] = len(re.findall("可永久使用",html))

        # 时装风格
        item['shizhuang_name'] = ",".join(list(set([i[1] for i in re.findall("#(cbe38ff|B)(.{0,5}风格)",html)])))

        #所在区服
        item['area'] = re.findall(r'所在区服：(.*?)&nbsp',html)[0]

        #神器星级
        try:
            item['shenqi_star'] = max(list(map(int,re.findall(r'"icon":"Shenqi.*?"xingJi":(\d),',html))))
        except:
            item['shenqi_star'] = 9

        # #稀有坐骑统计
        # zuoji_list = re.findall(r'"name":"坐骑：(.*?)".*?"guiZhong":(\d).*?"useTimeDesc2":"该物品将在0年0月(\d)日24点消失",',html)
        # zuoji_true = []
        # for zuoji in zuoji_list:
        #     if zuoji[1] == "1" and zuoji[2] == "0":
        #         zuoji_true.append(zuoji[0])
        # item["zuoji"] = ",".join(zuoji_true)
        # #稀有座机数量
        # item["zuoji_num"] = len(zuoji_true)
        #重楼数量
        item["chonglou_num"] = len(re.findall(r'"name":"重楼(.+?)"',html))

        wai_attack = int(response.xpath('//*[@id="goods-detail"]/div/div[2]/div/div[10]/span/text()').extract_first().replace(" ", ""))
        nei_attack = int(response.xpath('//*[@id="goods-detail"]/div/div[2]/div/div[11]/span/text()').extract_first().replace(" ", ""))
        item["neiwai_max_attack"] = max(wai_attack, nei_attack)


        #橙色金色真元数量
        zhenyuanList = re.findall(r'data-grade="(\d+)"',html)
        item['orange_zhenyuan'] = zhenyuanList.count('5') + zhenyuanList.count('6')

        item['name'] = response.xpath("//*[@id='goods-detail']/div/div[2]/div/div[1]/span/text()").extract_first()
        item['menpai'] = response.xpath('//*[@id="goods-detail"]/div/div[1]/div/span[28]/text()').extract_first()[3:]
        item['cloth_grade'] = int(response.xpath('//*[@id="goods-detail"]/div/div[1]/div/span[27]/text()[1]').extract_first()[5:])
        if item['price']/item['cloth_grade'] < 0.01 or (int(item['price']) < 6000 and int(item['cloth_grade'])>400000 ) or int(item['cloth_grade'])>500000:
            return
        item['stone_grade'] = int(response.xpath('//*[@id="goods-detail"]/div/div[4]/div[1]/div/div[6]/span/text()').extract_first())
        item['level'] = int(response.xpath('//*[@id="goods-detail"]/div/div[1]/div/span[27]/text()[2]').extract_first()[3:])
        item['hp'] = int(response.xpath('//*[@id="goods-detail"]/div/div[2]/div/div[2]/span/i/text()').extract_first())
        bing = int(response.xpath('//*[@id="bing"]/div[2]/div/p[1]/text()').extract_first()[5:])
        huo = int(response.xpath('//*[@id="huo"]/div[2]/div/p[1]/text()').extract_first()[5:])
        xuan = int(response.xpath('//*[@id="xuan"]/div[2]/div/p[1]/text()').extract_first()[5:])
        du = int(response.xpath('//*[@id="du"]/div[2]/div/p[1]/text()').extract_first()[5:])
        shuxing_list = [bing,huo,xuan,du]
        attack_heightest_value = max(shuxing_list)
        pos = [bing,huo,xuan,du].index(attack_heightest_value)
        if pos == 0:
            height_shuxing = '冰属性'
        elif pos == 1:
            height_shuxing = '火属性'
        elif pos == 2:
            height_shuxing = '玄属性'
        elif pos == 3:
            height_shuxing = '毒属性'
        del shuxing_list[pos]

        kang_list = list(map(int,[re.findall(r'\d+',i)[0] for i in response.xpath('//div[@class="model"]/div[@class="c-o-l"]/p[2]/text()').extract()[:4]]))
        kang_max = max(kang_list)
        kang_pos = kang_list.index(kang_max)
        if kang_pos == 0:
            height_kang = '冰抗'
        elif kang_pos == 1:
            height_kang = '火抗'
        elif kang_pos == 2:
            height_kang = '玄抗'
        elif kang_pos == 3:
            height_kang = '毒抗'

        wanbao_list = response.xpath(r'//script[contains(@id,"gt_")]//text()')
        wanbao_value = 0
        for wanbao in wanbao_list:
            value_list = re.findall('.抗性 \+(\d+)', wanbao.extract())
            if len(value_list) == 0:
                continue
            wanbao_value += int(value_list[0])


        item['kang_heightest_value'] = kang_max + wanbao_value
        item['kang_heightest_name'] = height_kang
        item['attack_heightest_value'] = attack_heightest_value
        item['attack_heightest_name'] = height_shuxing
        item['others_attack'] = sum(shuxing_list)
        item['attack_all_value'] = item['attack_heightest_value'] + item['others_attack']
        item['attack_stab'] = int(response.xpath('//*[@id="sword"]/div[2]/div/p/text()').extract_first()[6:])
        item['huixin'] = int(response.xpath('//*[@id="goods-detail"]/div/div[2]/div/div[17]/span/text()').extract_first())
        item['mingzhong'] = int(response.xpath('//*[@id="goods-detail"]/div/div[2]/div/div[14]/span/text()').extract_first().replace(" ",""))
        item['shanbi'] = int(response.xpath('//*[@id="goods-detail"]/div/div[2]/div/div[15]/span/text()').extract_first().replace(" ",""))
        item['tili_d'] = re.findall('<p>体力：\+\r\n\d*',html)[0].split("\n")[1]

        # 寻找属性鼎
        a = re.findall('sd r">\d*', html)
        b = []
        for i in a:
            b.append(int(i.split(">")[1]))
        item['shuxing_d'] = max(b)
        print(b)

        # 7级雕文，6级雕文等级
        item['diaowen8'] = len(re.findall('雕纹8级',html))
        item['diaowen7'] = len(re.findall('雕纹7级',html))
        item['diaowen6'] = len(re.findall('雕纹6级', html))

        #元宝数量
        item['yuanbao'] = int(re.findall('<div class="row2">所有元宝：<span class="span">(\d+)</span></div>',html)[0])

        #8，9星装备数量
        text = re.findall('"equip".*?"18"',html)[0]
        item['star8'] = len(re.findall('"xingJi":8|"xingJi":9',text))

        #体力身法获取
        item["tili"] = int(re.findall(r'<div class="row2">体力：<span class="span">(\d+) <b class="plus">',html)[0])
        item["shenfa"] = int(re.findall(r'<div class="row2">身法：<span class="span">(\d+) <b class="plus">',html)[0])

        # 稀有心决获取
        item["nb_xinjue_name"] = ",".join(list(set(re.findall(r'("鼎湖龙吟"|"四面楚歌")', html))))
        item["nb_xinjue_num"] = len(list(set(re.findall(r'("鼎湖龙吟"|"四面楚歌")', html))))

        # # 秘技获取
        # item["miji"] = ""
        # miji_list = response.xpath('//*[@class="tab-cont-item vitality"]/div[4]//div[@class="method-info"]/p/text()')
        # miji_level_list = response.xpath('//*[@class="tab-cont-item vitality"]/div[4]//i[@class="dengji"]/text()')
        # for miji_num in range(len(miji_list)):
        #     item["miji"] += "%s[%s]"%(miji_list[miji_num], miji_level_list[miji_num])
        yield item
