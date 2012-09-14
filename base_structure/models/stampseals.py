# coding= utf-8
from django.db import models


class StampSeals(models.Model):                                      # Марка пломба.
    series = models.CharField(u'серия',                              # Серия марки, буквеное обозначение вида: 'AA'.
                                max_length=2)

    number = models.CharField(u'номер',
             max_length=7,
             unique=True)

    year = models.CharField(u'год', max_length=4)

    QUARTERS = ((u'первый квартал', u'первый'),
                (u'второй квартал', u'второй'),
                (u'третий квартал', u'третий'),
                (u'третий квартал', u'четвёртый'))

    quarter = models.CharField(max_length=14,
                                   verbose_name='квартал',
                                   choices=QUARTERS)

    STATUS = ((u'установлена',    u'установлена'),
              (u'не установлена', u'не установлена'),
              (u'использована',   u'использована'))

    status = models.CharField(max_length=14,
                              verbose_name='статус',
                              choices=STATUS)

    def __unicode__(self):
        return u'%s,  %s,  %s,  %s' % (self.status,
                                       self.year,
                                       self.number,
                                       self.quarter,)

    class Meta:
        verbose_name_plural = u"марки пломбы"

        verbose_name = u"марка пломба"

        app_label = 'base_structure'

        ordering = (u'series', u'number',
                     u'year', u'quarter')
