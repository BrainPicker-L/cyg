from role.models import Role
from django.shortcuts import render
from .forms import SelectForm
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator
from django.conf import settings
import re


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



def role2(request):
    context = {}
    lowPrice = request.GET.get("lowPrice",100)
    heightPrice = request.GET.get("heightPrice",10000001)
    sel_value = request.GET.get("sel_value","全部")
    verbose_name = request.GET.get("verbose_name","装备评分")

    if sel_value == "全部":
        context["roles"] = Role.objects.all()
    else:
        context["roles"] = Role.objects.filter(menpai=sel_value)
    if lowPrice and heightPrice and (lowPrice != "None" and heightPrice != "None"):
        context["lowPrice"] = lowPrice
        context["heightPrice"] = heightPrice
        context["roles"] = context["roles"].filter(price__gte=lowPrice)
        context["roles"] = context["roles"].filter(price__lte=heightPrice)
    context["request_url"] = re.sub(r'page=\d+&',"",request.get_full_path().split("/")[-1][1:])
    context["request_url_all"] = re.sub(r'&verbose_name=.+','',request.get_full_path())
    print(context["request_url_all"])


    context["verbose_names"] = [name.verbose_name for name in context["roles"][0]._meta.fields][1:]
    context["true_names"] = [name.name for name in context["roles"][0]._meta.fields][1:]
    num = context["verbose_names"].index(verbose_name)
    print(context["true_names"][num])
    context["roles"] = context["roles"].order_by("-"+context["true_names"][num])

    context["roles"], context["page_of_roles"], context["page_range"] = get_role_list_common_data(request,context["roles"])




    context["select_form"] = SelectForm()
    return render(request,"role.html",context)