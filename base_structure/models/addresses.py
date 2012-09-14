# coding= utf-8
from django.db import models


class Addresses(models.Model):
    address = models.CharField(u'адрес',
                max_length=255, blank=True)

    def __unicode__(self):
        return u'%s' % (self.address)

    class Meta:
        app_label = 'base_structure'
        verbose_name_plural = u'адреса'
        verbose_name = u'адрес'
        #ordering = ('',)
