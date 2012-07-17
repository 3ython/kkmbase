# coding= utf-8
from django.db import models

from base_structure.models.stampseals    import StampSeals
from base_structure.models.svkgr         import SVKGR
from base_structure.models.svkso         import SVKSO
from base_structure.models.eklz          import EKLZ
from base_structure.models.organizations import Organizations

class Registrators(models.Model):                                    # Фискальный регистратор. (fiscal registrar)

    modelname = models.CharField(u'модель', 
          blank=True, max_length=255)

    factorynumber = models.CharField(u'заводской номер', 
          blank=True, max_length=255, unique=True)

    registrnumber = models.CharField(u'регистрационный  номер',      # Регистрационный номер.
                    blank=True, max_length=255)

    stampseals = models.OneToOneField(StampSeals, 
                           null=True, blank=True)

    svkgr = models.ForeignKey(SVKGR,                               # идентификатор госреестра. (Visual ID state register) 
                           blank=True, null=True)

    svkso = models.ForeignKey(SVKSO,                               # идентификатор сервисного обслуживания. (Visual service ID)
                           blank=True, null=True)

    eklz  = models.ForeignKey(EKLZ,                                # Электронная контрольная лента защищенная. (Electronic control tape is protected)
                           blank=True, null=True)
                              
    version = models.CharField(u'номер версии',
            max_length=255, blank=True)

    organization = models.ForeignKey(Organizations,
                            blank=True, null=True)

    workplace = models.CharField(u'место установки',
                max_length=255, blank=True)

    
    def __unicode__(self):
        return u'%s, %s, %s, %s' % (self.factorynumber,
                                    self.modelname, 
                                    self.version, 
                                    self.registrnumber)
    class Meta:
        verbose_name_plural = u'регистраторы'

        app_label           =  'base_structure'

        verbose_name        = u'регистратор'
        #ordering = ('',)
        
