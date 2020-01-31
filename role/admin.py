from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(visitNums)
class visitNumsAdmin(admin.ModelAdmin):
    list_display = ('name','visitnumsAll')
@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    list_display = ('id','name')