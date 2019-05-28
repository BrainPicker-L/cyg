from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.models import User
from django.urls import reverse
from django.http import JsonResponse
from .forms import LoginForm, RegForm, ChangeNicknameForm, ChangeStatement
from .models import Profile



def login_for_medal(request):
    login_form = LoginForm(request.POST)
    data = {}
    if login_form.is_valid():
        user = login_form.cleaned_data['user']
        auth.login(request, user)
        data['status'] = 'SUCCESS'
    else:
        data['status'] = 'ERROR'
    return JsonResponse(data)


def login(request):
    if request.method == 'POST':
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            user = login_form.cleaned_data['user']
            auth.login(request, user)
            return redirect('role')
    else:
        login_form = LoginForm()

    context = {}
    context['login_form'] = login_form
    return render(request, 'login.html', context)


def register(request):
    if request.method == 'POST':
        reg_form = RegForm(request.POST)
        if reg_form.is_valid():
            username = reg_form.cleaned_data['username']
            email = reg_form.cleaned_data['email']
            password = reg_form.cleaned_data['password']
            # 创建用户
            user = User.objects.create_user(username, email, password)
            user.save()
            # 登录用户
            user = auth.authenticate(username=username, password=password)
            auth.login(request, user)
            return redirect('role')
    else:
        reg_form = RegForm()

    context = {}
    context['reg_form'] = reg_form
    return render(request, 'register.html', context)


def logout(request):
    auth.logout(request)
    return redirect('index')


def user_info(request):
    context = {}
    return render(request, 'user_info.html', context)


def change_nickname(request):
    if request.method == 'POST':
        form = ChangeNicknameForm(request.POST,user=request.user)
        print(request.user)
        if form.is_valid():
            nickname_new = form.cleaned_data['nickname_new']
            profile,created = Profile.objects.get_or_create(user=request.user)
            profile.nickname = nickname_new
            profile.save()
            return redirect('user_info')
    else:
        form = ChangeNicknameForm()

    context = {}
    context["page_title"] = "修改昵称"
    context["form_title"] = "修改昵称"
    context["submit_value"] = "修改"
    context["form"] = form
    return render(request,'form.html',context)

def change_statement(request):
    if request.method == 'POST':
        form = ChangeStatement(request.POST,user=request.user)
        print(form)
        if form.is_valid():
            statement_new = form.cleaned_data['statement_new']
            profile,created = Profile.objects.get_or_create(user=request.user)
            profile.statement = statement_new
            profile.save()
            return redirect('user_info')
    else:
        form = ChangeStatement()

    context = {}
    context["page_title"] = "修改个人简介"
    context["form_title"] = "修改个人简介"
    context["submit_value"] = "修改"
    context["form"] = form
    return render(request,'form.html',context)