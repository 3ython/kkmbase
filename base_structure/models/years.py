
# coding= utf-8
from django.db import models


class Year(models.Model):

    year = models.CharField(u'Год', max_length=4)

    def __unicode__(self):
        return u'%s' % (self.year)

    class Meta:
        verbose_name_plural = u"годa"

        verbose_name = u"год"

        app_label = 'base_structure'

#        ordering  = (u'year')
