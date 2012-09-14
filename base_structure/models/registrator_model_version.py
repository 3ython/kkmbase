# coding= utf-8
from django.db import models


class Registrator_model_version(models.Model):

    version = models.CharField(u'версия',
            max_length=255, unique=True)

    def __unicode__(self):
        return u'(версия %s)' % (self.version, )

    class Meta:
        verbose_name_plural = u'версия'

        app_label = 'base_structure'

        verbose_name = u'версия'
        #ordering = ('',)
