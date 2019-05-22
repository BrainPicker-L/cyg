# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy_djangoitem import DjangoItem
from role.models import Role
# class CygspiderItem(scrapy.Item):
#     price = scrapy.Field()
#     name = scrapy.Field()
#     menpai = scrapy.Field()
#     cloth_grade = scrapy.Field()
#     stone_grade = scrapy.Field()
#     level = scrapy.Field()
#     hp = scrapy.Field()
#     attack_heightest_name = scrapy.Field()
#     attack_heightest_value = scrapy.Field()
#     others_attack = scrapy.Field()
#     attack_stab = scrapy.Field()
#     detail_url = scrapy.Field()
class RoleItem(DjangoItem):
    django_model = Role