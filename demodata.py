
# -*- coding: utf-8 -*-
# @Date    : 2015-07-28 20:38:38
# @Author  : Weizhong Tu (mail@tuweizhong.com)
# @Link    : http://www.tuweizhong.com
#http://www.ziqiangxuetang.com/django/django-cms-develop2.html
'''
create some records for demo database
'''

from thatsStore.wsgi import *
from xstores.models import XStore
from xstores.xgoods.xgoods import XGoods

from django.contrib import auth
def main():
    columns_urls = [
        ('商家1', '商家1'),
        ('商家2', '商家2'),
        ('商家3', '商家3'),
    ]
    a = auth.models.User.objects.all()[0]
    for column_name, url in columns_urls:
        print(column_name)
        c = XStore.objects.get_or_create(name=column_name,author=a, slug=url)[0]

        # goods
        for i in range(1, 11):
            print('xgoods_{}'.format(i))
            xgoods = XGoods.objects.get_or_create(name='{}_{}'.format(column_name, i),
                slug='xgoods_{}_{}'.format(column_name, i),
                prize='2.0',
                xstore = c,
                intro='详细介绍： {} {}'.format(column_name, i))[0]
            #xgoods.xstore.add(c)


if __name__ == '__main__':
    main()
    print("Done!")