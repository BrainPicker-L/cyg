from role.models import Role
from django.shortcuts import render
from .forms import SelectForm
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator
from django.conf import settings
def role(request):
    context = {}
    context["lowPrice"] = None
    context["heightPrice"] = None

    if request.method=="GET":
        try:
            context["select_menpai"] = "全部"
            context["roles"] = Role.objects.all()
            context["verbose_names"] = [name.verbose_name for name in context["roles"][0]._meta.fields][1:]
            context["true_names"] = [name.name for name in context["roles"][0]._meta.fields]
        except:
            context["roles"] = []
            context["verbose_names"] = []
            context["true_names"] = []
    elif request.method=="POST":
        select_form = SelectForm(request.POST)
        try:
            if select_form.is_valid():
                lowPrice = select_form.cleaned_data["lowPrice"]
                heightPrice = select_form.cleaned_data["heightPrice"]
                get_value = request.POST.get('sel_value', "")
                if get_value == "全部":
                    context["roles"] = Role.objects.all()
                else:
                    context["roles"] = Role.objects.filter(menpai=get_value)
                if lowPrice and heightPrice and (lowPrice!="None" and heightPrice!="None"):
                    context["lowPrice"] = lowPrice
                    context["heightPrice"] = heightPrice
                    context["roles"] = context["roles"].filter(price__gte=lowPrice)
                    context["roles"] = context["roles"].filter(price__lte=heightPrice)
                context["select_menpai"] = get_value
                context["verbose_names"] = [name.verbose_name for name in context["roles"][0]._meta.fields][1:]
                context["true_names"] = [name.name for name in context["roles"][0]._meta.fields]
            else:
                pass
        except:
            get_value = request.POST.get('sel_value', "")
            context["roles"] = []
            context["verbose_names"] = []
            context["true_names"] = []
            context["select_menpai"] = get_value
    context["roles"], context["page_of_roles"], context["page_range"] = get_role_list_common_data(request,context["roles"])
    context["select_form"] = SelectForm(initial={'lowPrice': '100','heightPrice': '10000001', 'menpai':'全部'})
    return render(request, "role.html", context)

def role_sort(request,menpai,verbose_name,lowPrice,heightPrice):
    context = {}
    context["lowPrice"] = lowPrice
    context["heightPrice"] = heightPrice
    if request.method == "GET":
        if menpai == "全部":
            context["roles"] = Role.objects.all()
        else:
            context["roles"] = Role.objects.filter(menpai=menpai)
        if lowPrice and heightPrice and (lowPrice!="None" and heightPrice!="None"):
            context["roles"] = context["roles"].filter(price__gte=lowPrice)
            context["roles"] = context["roles"].filter(price__lte=heightPrice)
        context["select_menpai"] = menpai
        context["verbose_names"] = [name.verbose_name for name in context["roles"][0]._meta.fields][1:]
        context["true_names"] = [name.name for name in context["roles"][0]._meta.fields][1:]
        num = context["verbose_names"].index(verbose_name)
        context["roles"] = context["roles"].order_by("-"+context["true_names"][num])
    elif request.method == "POST":
        select_form = SelectForm(request.POST)
        try:
            if select_form.is_valid():
                get_lowPrice = select_form.cleaned_data["lowPrice"]
                get_heightPrice = select_form.cleaned_data["heightPrice"]
                get_value = request.POST.get('sel_value', "")
                print(get_value,get_heightPrice,get_lowPrice)
                if get_value == "全部":
                    context["roles"] = Role.objects.all()
                else:
                    context["roles"] = Role.objects.filter(menpai=get_value)
                if get_lowPrice and get_heightPrice and (get_lowPrice!="None" and get_heightPrice!="None"):
                    context["roles"] = context["roles"].filter(price__gte=get_lowPrice)
                    context["roles"] = context["roles"].filter(price__lte=get_heightPrice)
                context["select_menpai"] = get_value
                context["lowPrice"] = get_lowPrice
                context["heightPrice"] = get_heightPrice
                context["verbose_names"] = [name.verbose_name for name in context["roles"][0]._meta.fields][1:]
                context["true_names"] = [name.name for name in context["roles"][0]._meta.fields]
            else:
                pass
        except:
            get_value = request.POST.get('sel_value', "")
            context["roles"] = []
            context["verbose_names"] = []
            context["true_names"] = []
            context["select_menpai"] = get_value
    context["roles"],context["page_of_roles"],context["page_range"] = get_role_list_common_data(request, context["roles"])
    context["select_form"] = SelectForm(initial={'lowPrice': '100','heightPrice': '10000001', 'menpai':'全部'})
    return render(request, "role.html", context)

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