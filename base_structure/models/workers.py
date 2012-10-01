# coding= utf-8

from django.db import models
from base_structure.models.workers_status import Workers_status


class Workers(models.Model):

    name = models.CharField(u'Ф.И.О.',
                             max_length=255,
                             unique=True)

    status = models.ForeignKey(Workers_status,
                  verbose_name=u'должность',
                  unique=True,
                  blank=True,
                  null=True
                  )

    def __unicode__(self):
        return u'%s,    %s' % (self.name,
                               self.status,)

    class Meta:
        verbose_name_plural = u'сотрудники'
        app_label = 'base_structure'
        verbose_name = u'сотрудник'
