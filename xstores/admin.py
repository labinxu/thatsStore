from django.contrib import admin
#import xadmin
# Register your models here.
from .xgoods.xgoods import XGoods

from .models import XStore

class XStoreAdmin(admin.ModelAdmin):
    list_display = ('name', 'author', 'create_date','nav_display', 'home_display')


class XGoodsAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'prize','add_date')





admin.site.register(XStore, XStoreAdmin)
admin.site.register(XGoods, XGoodsAdmin)
