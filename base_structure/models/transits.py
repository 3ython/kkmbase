# coding= utf-8
from django.db import models

class Transits(models.Model):
    transit = models.CharField(u'маршрут проезда',
                     max_length=255, 
                     unique=True,
                     blank=True)

    def __unicode__(self):
        return u'%s' % (self.transit )
    class Meta:
        app_label = 'base_structure'
        verbose_name = u"маршруты проезда"
        verbose_name_plural = u"маршрут проезда"
       #ordering = ('',)
