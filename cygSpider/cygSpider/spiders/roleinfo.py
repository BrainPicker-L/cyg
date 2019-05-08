# -*- coding: utf-8 -*-
import scrapy
from cygSpider.items import RoleItem
import re
import time
from role.models import *
class RoleinfoSpider(scrapy.Spider):
    name = 'roleinfo'
    allowed_domains = ['changyou.com']
    start_urls = ['http://tl.cyg.changyou.com/goods/selling?world_id=0&gem_level=3&gem_num=72&have_chosen=gem_level*3&page_num=1#goodsTag']
    def parse(self, response):
        li_list = response.xpath("//ul[@class='pg-goods-list']/li")
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
        print(next_url)
        if next_url != '':
            yield scrapy.Request(
                next_url,
                callback=self.parse,
                dont_filter=False
            )


    def parse_detail(self, response):   #处理详情页
        item = response.meta["item"]
        html = response.body.decode('utf-8')



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



        item['name'] = response.xpath("//*[@id='goods-detail']/div/div[2]/div/div[1]/span/text()").extract_first()
        item['menpai'] = response.xpath('//*[@id="goods-detail"]/div/div[1]/div/span[28]/text()').extract_first()[3:]
        item['cloth_grade'] = int(response.xpath('//*[@id="goods-detail"]/div/div[1]/div/span[27]/text()[1]').extract_first()[5:])
        item['stone_grade'] = int(response.xpath('//*[@id="goods-detail"]/div/div[4]/div[1]/div/div[6]/span/text()').extract_first())
        item['level'] = int(response.xpath('//*[@id="goods-detail"]/div/div[1]/div/span[27]/text()[2]').extract_first()[3:])
        item['hp'] = int(response.xpath('//*[@id="goods-detail"]/div/div[2]/div/div[3]/span/i/text()').extract_first())
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

        item['attack_heightest_value'] = attack_heightest_value
        item['attack_heightest_name'] = height_shuxing
        item['others_attack'] = sum(shuxing_list)
        item['attack_stab'] = int(response.xpath('//*[@id="sword"]/div[2]/div/p/text()').extract_first()[6:])
        item['huixin'] = int(response.xpath('//*[@id="goods-detail"]/div/div[2]/div/div[17]/span/text()').extract_first())
        item['mingzhong'] = int(response.xpath('//*[@id="goods-detail"]/div/div[2]/div/div[15]/span/text()').extract_first().replace(" ",""))
        item['shanbi'] = int(response.xpath('//*[@id="goods-detail"]/div/div[2]/div/div[16]/span/text()').extract_first().replace(" ",""))
        item['tili_d'] = re.findall('<p>体力：\+\r\n\d*',html)[0].split("\n")[1]

        # 寻找属性鼎
        a = re.findall('sd r">\d*', html)
        b = []
        for i in a:
            b.append(int(i.split(">")[1]))
        item['shuxing_d'] = max(b)
        print(b)
        yield item
