from django.db import models

# Create your models here.
class Role(models.Model):
    if30 = models.IntegerField(verbose_name='三十附体',default=0)
    price = models.IntegerField(verbose_name='价格')
    name = models.CharField(verbose_name='角色名', max_length=30)
    menpai = models.CharField(verbose_name='门派',max_length=20)
    cloth_grade = models.IntegerField(verbose_name='装备评分')
    stone_grade = models.IntegerField(verbose_name='宝石评分')
    level = models.IntegerField(verbose_name='等级')
    hp = models.IntegerField(verbose_name='血上限')
    attack_heightest_name = models.CharField(verbose_name='最高属性攻击名称', max_length=30)
    attack_heightest_value = models.IntegerField(verbose_name='最高属性攻击值')
    others_attack = models.IntegerField(verbose_name='副属性攻击')
    attack_stab = models.IntegerField(verbose_name='穿刺攻击')
    huixin = models.IntegerField(verbose_name='会心')
    mingzhong = models.IntegerField(verbose_name='命中')
    shanbi = models.IntegerField(verbose_name='闪避')
    detail_url = models.CharField(verbose_name='详情链接', max_length=100)
    tili_d = models.IntegerField(verbose_name='体力鼎',default=0)
    shuxing_d = models.IntegerField(verbose_name='属性鼎',default=0)
    wuhun = models.IntegerField(verbose_name="武魂",default=0)
    if20 = models.IntegerField(verbose_name="双十珍兽",default=0)
    cailiao_3 = models.IntegerField(verbose_name="三级材料",default=0)
    shizhuang_num = models.IntegerField(verbose_name="时装数量",default=0)
    area = models.CharField(verbose_name="区服", max_length=200, default='')
    shenqi_star = models.IntegerField(verbose_name="神器星级",default=0)
    neiwai_max_attack = models.IntegerField(verbose_name="最高内外功",default=0)
    orange_zhenyuan = models.IntegerField(verbose_name='橙色金色真元数量',default=0)
    kang_heightest_name = models.CharField(verbose_name="最高抗性名称",max_length=30,default="")
    kang_heightest_value = models.IntegerField(verbose_name="最高抗性值",default=0)
    zuoji = models.CharField(verbose_name="稀有坐骑",max_length=200,default='')

    chonglou_num = models.IntegerField(verbose_name="重楼个数",default=0)
    zuoji_num = models.IntegerField(verbose_name="稀有坐骑数量", default=0)


class visitNums(models.Model):
    name = models.CharField(verbose_name="名称",default="",max_length=50)
    visitnumsAll = models.IntegerField(verbose_name="总访问次数",default=0)