# coding= utf-8
from django.db import models

class Workers_status(models.Model):

    status = models.CharField(u'должность',
                     max_length=255, 
                     unique=True)
                     
    def __unicode__(self):
        return u'%s' % (self.status)
    class Meta:
        app_label = 'base_structure'
        verbose_name = u"должность сотрудника"
        verbose_name_plural = u"должности сотрудников"
       #ordering = ('',)
