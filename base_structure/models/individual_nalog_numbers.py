# coding= utf-8
from django.db import models

class Individual_nalog_numbers(models.Model):
    inn = models.CharField(u'ИНН',
                     max_length=255, 
                     unique=True,
                     blank=True)
                     
    def __unicode__(self):
        return u'%s' % (self.inn)
    class Meta:
        app_label = 'base_structure'
        verbose_name = u"ИНН"
        verbose_name_plural = u"ИНН"
       #ordering = ('',)
