from role.models import Role
from django.shortcuts import render
from .forms import SelectForm
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator
def role(request):
    context = {}
    context["lowPrice"] = None
    context["heightPrice"] = None

    if request.method=="GET":

        context["select_menpai"] = "全部"
        context["roles"] = Role.objects.all()
        context["verbose_names"] = [name.verbose_name for name in context["roles"][0]._meta.fields][1:]
        context["true_names"] = [name.name for name in context["roles"][0]._meta.fields]

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
    context["select_form"] = SelectForm(initial={'lowPrice': '100','heightPrice': '10000001', 'menpai':'全部'})
    return render(request, "role.html", context)

