from ..models import XStore
nav_xstores = XStore.objects.filter(nav_display=True)


def NavXstores(request):
    return {'nav_display_xstores': nav_xstores}