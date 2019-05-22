# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


from role.models import *
class CygspiderPipeline(object):
    def process_item(self, item, spider):
        item.save()
        return item
    # def process_item(self, item, spider):
    #     #collection.insert(dict(item))
    #     print(item)
    #     a = Menpai.objects.all()
    #
    #     for i, j in enumerate(a):
    #         if j.menpai_name == item['menpai']:
    #             item['menpai'] = a[i]
    #     Role.objects.create(price=item['price'], name=item['name'], menpai=item['menpai'],
    #                         cloth_grade=item['cloth_grade'], stone_grade=item['stone_grade'],
    #                         level=item['level'], hp=item['hp'],
    #                         attack_heightest_name=item['attack_heightest_name'],
    #                         attack_heightest_value=item['attack_heightest_value'],
    #                         others_attack=item['others_attack'], attack_stab=item['attack_stab'],
    #                         detail_url=item['detail_url'], )
    #
    #     return item
