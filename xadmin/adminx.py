import xadmin
from .models import UserSettings
from xadmin.layout import *


class UserSettingsAdmin(object):
    model_icon = 'fa fa-cog'
    hidden_menu = True

class GlobalSetting(object):
    site_title = 'MyTitle'
    site_footer = 'MyFooter'

xadmin.site.register(UserSettings, UserSettingsAdmin)
xadmin.site.register(xadmin.views.CommAdminView,GlobalSetting)
