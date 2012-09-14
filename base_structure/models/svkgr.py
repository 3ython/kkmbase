# coding= utf-8
from django.db import models

class SVKGR(models.Model):                                                    # Визуальный идентификатор государственного реестра. (Visual ID state register)

    number = models.CharField(max_length=7,
                              verbose_name='номер',
                              unique=True)

    year = models.CharField(max_length=4,
                            verbose_name='год',
                            unique=True)

    STATUS = ((u'у', u'установлена'),
              (u'н', u'не установлена'),
              (u'и', u'использована'))

    status = models.CharField(max_length=1,
                              verbose_name='статус',
                              choices=STATUS)

    def __unicode__(self):
        return u'%s,    %s,    %s' % (self.year,
                                      self.number,
                                      self.status)

    class Meta:

        verbose_name_plural = u'СВК госреестра'

        verbose_name = u'СВК госреестра'

        app_label = 'base_structure'

        ordering = (u'number', u'year')
