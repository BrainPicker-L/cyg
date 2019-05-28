from django.contrib import admin
from .models import visitNums
# Register your models here.
@admin.register(visitNums)
class visitNumsAdmin(admin.ModelAdmin):
    list_display = ('name','visitnumsAll')