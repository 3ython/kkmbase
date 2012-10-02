
# coding= utf-8
from django.db import models


class Passport_version(models.Model):

    number = models.CharField(u'паспорт версии', 
                        max_length=10,
                        unique=True,)

    def __unicode__(self):
        return u'%s' % (self.year)

    class Meta:
        verbose_name_plural = u"номера паспортов версий"

        verbose_name = u"номера паспорта версии"

        app_label = 'base_structure'

#        ordering  = (u'year')
