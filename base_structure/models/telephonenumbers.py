# coding= utf-8
from django.db import models


class TelephoneNumbers(models.Model):
    phonenumber = models.CharField( u'телефонный номер',
                                   max_length=255,
                                   unique=True)

    def __unicode__(self):
        return u'%s' % (self.phonenumber)

    class Meta:
        verbose_name_plural = u"телефоны"
        app_label = 'base_structure'
        verbose_name = u"телефон"
       #ordering = ('',)
