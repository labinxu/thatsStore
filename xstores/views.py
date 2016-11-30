from django.shortcuts import render
from django.http import HttpResponse
# Create your views her
from .models import XStore
from .xgoods.xgoods import XGoods
from django.shortcuts import redirect


def index(request):
    home_display_xstores = XStore.objects.filter(home_display=True)
    nav_display_xstores = XStore.objects.filter(nav_display=True)

    return render(request, 'index.html',
                  {
                      'home_display_xstores':home_display_xstores,
                      'nav_display_xstores':nav_display_xstores,
                  })

   # xstores = XStore.objects.all()
   # return render(request, 'index.html', {'xstores': xstores})


def xstore_detail(request, xstore_slug):

    xstore = XStore.objects.get(slug=xstore_slug)
    return render(request, 'xstores/xstore.html', {'xstore': xstore})

def xgoods_detail(request, pk, xgoods_slug):
    xgoods = XGoods.objects.get(pk=pk)
    if(xgoods_slug != xgoods.slug):
        return redirect(xgoods, permanent=True)

    return render(request, 'xstores/goods_detail.html', {'xgoods': xgoods})