# coding= utf-8
from django.db import models


class Organizations_ownernames(models.Model):
    ownername = models.CharField(u'название организации',
                     max_length=255,
                     unique=True,
                     blank=True)

    def __unicode__(self):
        return u'%s' % (self.ownername)

    class Meta:
        app_label = 'base_structure'
        verbose_name_plural = u'названия организаций'
        verbose_name = u'название организации'
        #ordering = ('',)
