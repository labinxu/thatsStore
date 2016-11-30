from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse

# Create your models here.
class XStore(models.Model):
    sid = models.AutoField(primary_key=True, verbose_name=_("id"))
    name = models.CharField(max_length=20, verbose_name=_('名称'))
    slug = models.CharField('网址', max_length=256, db_index=True)
    intro = models.TextField(_('Introduce'), default='')

    author = models.ForeignKey('auth.User',on_delete=models.CASCADE, verbose_name=_('所有者'))
    create_date = models.DateTimeField(_('创建时间'), auto_now_add=True, editable=True)


    nav_display = models.BooleanField('导航显示', default=False)
    home_display = models.BooleanField('首页显示', default=False)

    def getAbsoluteUrl(self):
        return reverse('xstores', args=(self.slug, ))

    def __str__(self):
        return self.name

    class Meta:
        # order
        verbose_name = '商家'
        ordering =['name']
        verbose_name_plural = _('商家管理')
        #app_label = "我的应用"
