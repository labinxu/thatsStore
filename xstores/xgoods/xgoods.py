from django.db import models
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _
from DjangoUeditor.models import UEditorField
from ..models import XStore


class XGoods(models.Model):
    gid = models.AutoField(primary_key=True, verbose_name=_('Goods Id'))
    xstore = models.ForeignKey(XStore, on_delete=models.CASCADE, verbose_name="商家")
    prize = models.FloatField(verbose_name="价格",blank=True)
    name = models.CharField(max_length=20, verbose_name=_('名称'))
    slug = models.CharField(verbose_name='网址', max_length=256, unique=True)
    intro = UEditorField(_('说明'), height=300,
                         width=500,blank=True,imagePath="uploads/images/",
                         toolbars="besttome",
                         filePath='uploads/files/', default='')

    add_date = models.DateTimeField(_('添加日期'), auto_now_add=True, editable=True)

    def getAbsoluteUrl(self):
        return reverse('xgoods', args=(self.pk, self.slug))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('商品')
        verbose_name_plural = _('商品管理')
