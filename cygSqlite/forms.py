from django import forms


class SelectForm(forms.Form):
    SELVALUE = (
        ('全部门派', '全部'),
        ('少林', '少林'),
        ('明教', '明教'),
        ('丐帮', '丐帮'),
        ('武当', '武当'),
        ('峨嵋', '峨嵋'),
        ('星宿', '星宿'),
        ('天龙', '天龙'),
        ('天山', '天山'),
        ('逍遥', '逍遥'),
        ('慕容', '慕容'),
        ('唐门', '唐门'),
        ('鬼谷', '鬼谷'),
    )
    SELVALUE2 = (
        ('无等级限制','80-119'),
        ('80-89','80-89'),
        ('90-99','90-99'),
        ('100-119','100-119'),
    )

    SELVALUE3 = (
        ("无区服限制","无区服限制"),
        ("鸿运大区", "鸿运大区"),
        ("华中电信一区", "华中电信一区"),
        ("电信全国一区", "电信全国一区"),
        ("西南电信一区", "西南电信一区"),
        ("南部电信二区", "南部电信二区"),
        ("纵横双线", "纵横双线"),
        ("网通二区", "网通二区"),
        ("东北网通一区", "东北网通一区"),
        ("华东电信一区", "华东电信一区"),
        ("华东电信二区", "华东电信二区"),
        ("周年庆专区", "周年庆专区"),
        ("超级双线", "超级双线"),
        ("网通专区", "网通专区"),
        ("东部电信二区", "东部电信二区"),
        ("老友专区", "老友专区"),
        ("华北网通一区", "华北网通一区"),
        ("至尊电信", "至尊电信"),
        ("唯美双线", "唯美双线"),
        ("东部电信", "东部电信"),
        ("唯美电信", "唯美电信"),
        ("无双网通", "无双网通"),
        ("人气专区", "人气专区"),
    )
    lowPrice = forms.CharField(required=False)
    heightPrice = forms.CharField(required=False)
    sel_value = forms.CharField(max_length=10, widget=forms.widgets.Select(choices=SELVALUE))
    sel_value2 = forms.CharField(max_length=10, widget=forms.widgets.Select(choices=SELVALUE2))
    sel_value3 = forms.CharField(max_length=15, widget=forms.widgets.Select(choices=SELVALUE3))