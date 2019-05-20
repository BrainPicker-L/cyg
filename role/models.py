from django.db import models

# Create your models here.
class Role(models.Model):
    if30 = models.IntegerField('三十附体',default=0)
    price = models.IntegerField('价格')
    name = models.CharField('角色名', max_length=30)
    menpai = models.CharField('门派',max_length=20)
    cloth_grade = models.IntegerField('装备评分')
    stone_grade = models.IntegerField('宝石评分')
    level = models.IntegerField('等级')
    hp = models.IntegerField('血上限')
    attack_heightest_name = models.CharField('最高属性攻击名称', max_length=30)
    attack_heightest_value = models.IntegerField('最高属性攻击值')
    others_attack = models.IntegerField('副属性攻击')
    attack_stab = models.IntegerField('穿刺攻击')
    huixin = models.IntegerField('会心')
    mingzhong = models.IntegerField('命中')
    shanbi = models.IntegerField('闪避')
    detail_url = models.CharField('详情链接', max_length=100)
    tili_d = models.IntegerField('体力鼎',default=0)
    shuxing_d = models.IntegerField('属性鼎',default=0)
    wuhun = models.IntegerField("武魂",default=0)
    if20 = models.IntegerField("双十珍兽",default=0)
    cailiao_3 = models.IntegerField("三级材料",default=0)
    shizhuang_num = models.IntegerField("时装数量",default=0)
    area = models.CharField("区服", max_length=200, default='')
    shenqi_star = models.IntegerField("神器星级",default=0)