from django.db import models
from django.utils.translation import gettext_lazy as _
from ckeditor_uploader.fields import RichTextUploadingField


class Product(models.Model):
    title = models.CharField(verbose_name=_('title'), max_length=255)
    ingredients = RichTextUploadingField(verbose_name=_('Ingredients'))
    price = models.DecimalField(verbose_name=_('Price'), max_digits=6, decimal_places=2)

    class Meta:
        verbose_name = _('Product')
        verbose_name_plural = _('Products')
