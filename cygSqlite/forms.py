from django import forms


class SelectForm(forms.Form):
    SELVALUE = (
        ('全部', '全部'),
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
    lowPrice = forms.CharField(required=True)
    heightPrice = forms.CharField(required=True)
    sel_value = forms.CharField(max_length=10, widget=forms.widgets.Select(choices=SELVALUE))