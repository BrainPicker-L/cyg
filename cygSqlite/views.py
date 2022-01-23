from role.models import Role,visitNums
from django.shortcuts import render
from .forms import SelectForm
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator
from django.conf import settings
import re

def index(request):
    context = {}
    return render(request, "index.html", context)






def get_role_list_common_data(request, roles_all_list):
    paginator = Paginator(roles_all_list, settings.EACH_PAGE_ROLES_NUMBER)
    page_num = request.GET.get('page', 1) # 获取url的页面参数（GET请求）
    page_of_roles = paginator.get_page(page_num)
    currentr_page_num = page_of_roles.number # 获取当前页码
    # 获取当前页码前后各2页的页码范围
    page_range = list(range(max(currentr_page_num - 2, 1), currentr_page_num)) + \
                 list(range(currentr_page_num, min(currentr_page_num + 2, paginator.num_pages) + 1))
    # 加上省略页码标记
    if page_range[0] - 1 >= 2:
        page_range.insert(0, '...')
    if paginator.num_pages - page_range[-1] >= 2:
        page_range.append('...')
    # 加上首页和尾页
    if page_range[0] != 1:
        page_range.insert(0, 1)
    if page_range[-1] != paginator.num_pages:
        page_range.append(paginator.num_pages)
    roles = page_of_roles.object_list
    return roles,page_of_roles,page_range



def role(request):
    context = {}
    lowPrice = request.GET.get("lowPrice",100)
    heightPrice = request.GET.get("heightPrice",10000001)
    baoshiLevel = request.GET.get("baoshiLevel",0)
    zhenyuanNum = request.GET.get("zhenyuanNum",0)
    tili_d = request.GET.get("tili_d",0)
    shuxing_d = request.GET.get("shuxing_d",0)
    attack_heightest_value = request.GET.get("attack_heightest_value", 0)
    shizhuang_name = request.GET.get('shizhuang_name',"")
    nb_xinjue_name = request.GET.get('nb_xinjue_name',"")
    chonglou_num = request.GET.get('chonglou_num', 0)
    kang_heightest_value = request.GET.get('kang_heightest_value', 0)
    yigudan  = request.GET.get('yigudan', 0)

    menpai = request.GET.get("sel_value","全部")
    verbose_name = request.GET.get("verbose_name","装备评分")

    visitnum,judge = visitNums.objects.get_or_create(name="总搜索次数")
    print(baoshiLevel)
    if not judge:
        visitnum.visitnumsAll += 1
        visitnum.save()

    l_level,h_level = list(map(int,(request.GET.get("sel_value2","80-119").split("-"))))

    qufu = request.GET.get("sel_value3","无区服限制")


    if menpai == "全部":
        context["roles"] = Role.objects.all()#.exclude(menpai="峨嵋")
        context["roles"] = Role.objects.all().exclude(cloth_grade__gte=500000)
    else:
        context["roles"] = Role.objects.filter(menpai=menpai)

    main_shuxing = request.GET.get("sel_value4", "无主属性限制")
    if main_shuxing != "无主属性限制":
        context["roles"] = context["roles"].filter(attack_heightest_name=main_shuxing)
    context["roles"] = context["roles"].filter(level__gte=l_level).exclude(menpai="峨嵋")
    context["roles"] = context["roles"].filter(level__lte=h_level)
    if baoshiLevel and baoshiLevel != None:
        context["roles"] = context["roles"].filter(stone_grade__gte=baoshiLevel)
    if zhenyuanNum and zhenyuanNum != None:
        context["roles"] = context["roles"].filter(orange_zhenyuan__gte=zhenyuanNum)
    if tili_d and tili_d != None:
        context["roles"] = context["roles"].filter(tili_d__gte=tili_d)
    if shuxing_d and shuxing_d !=None:
        context["roles"] = context["roles"].filter(shuxing_d__gte=shuxing_d)
    if attack_heightest_value and attack_heightest_value != None:
        context["roles"] = context["roles"].filter(attack_heightest_value__gte=attack_heightest_value)
    if shizhuang_name and shizhuang_name != None:
        context["roles"] = context["roles"].filter(shizhuang_name__contains=shizhuang_name)
    if nb_xinjue_name and nb_xinjue_name != None:
        context["roles"] = context["roles"].filter(nb_xinjue_name__contains=nb_xinjue_name)
    if chonglou_num and chonglou_num != None:
        context["roles"] = context["roles"].filter(chonglou_num__gte=chonglou_num)
    if kang_heightest_value and kang_heightest_value != None:
        context["roles"] = context["roles"].filter(kang_heightest_value__gte=int(kang_heightest_value))

    if yigudan and yigudan != None:
        context["roles"] = context["roles"].filter(yigudan__gte=int(yigudan))

    if qufu != "无区服限制":
        context["roles"] = context["roles"].filter(area=qufu)
    if lowPrice and heightPrice and (lowPrice != "None" and heightPrice != "None"):
        context["lowPrice"] = lowPrice
        context["heightPrice"] = heightPrice
        context["roles"] = context["roles"].filter(price__gte=lowPrice)
        context["roles"] = context["roles"].filter(price__lte=heightPrice)

    context["request_url"] = re.sub(r'page=\d+&',"",request.get_full_path().split("/")[-1][1:])
    context["request_url_all"] = re.sub(r'&verbose_name=.+','',request.get_full_path())
    print(context["request_url_all"])
    print(verbose_name)
    try:
        context["verbose_names"] = [name.verbose_name for name in context["roles"][0]._meta.fields][1:-3]
        context["true_names"] = [name.name for name in context["roles"][0]._meta.fields][1:]
        num = context["verbose_names"].index(verbose_name)
        if verbose_name == "稀有坐骑":

            context["roles"] = context["roles"].order_by("-zuoji_num")
        else:
            context["roles"] = context["roles"].order_by("-" + context["true_names"][num])
    except:
        context["verbose_names"] = []
        context["true_names"] = []
        context["roles"] = []

    context["visitnum"] = visitnum.visitnumsAll
    context["roles"], context["page_of_roles"], context["page_range"] = get_role_list_common_data(request,context["roles"])


    context["select_form"] = SelectForm()
    return render(request,"role.html",context)