# coding= utf-8
from django.db import models


class Working_times(models.Model):

    working_time = models.CharField(u'название организации',
                                        max_length=255,
                                        unique=True,
                                        blank=True)

    def __unicode__(self):
        return u'%s' % (self.working_time)

    class Meta:
        app_label = 'base_structure'
        verbose_name = u"время работы"
        verbose_name_plural = u"часы работы"
       #ordering = ('',)
