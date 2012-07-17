# coding= utf-8
from django.db import models

class Registrator_models(models.Model):                    # Фискальный регистратор. (fiscal registrar)

    modelname = models.CharField(u'модель', 
          unique=True, max_length=255)

    def __unicode__(self):
        return u'  %s' % (self.modelname,)
        
    class Meta:
        verbose_name_plural = u'модели регистраторов'

        app_label           =  'base_structure'

        verbose_name        = u'модель регистратора'
        #ordering = ('',)
