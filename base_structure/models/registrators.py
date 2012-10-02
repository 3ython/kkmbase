# coding= utf-8
from django.db import models

from base_structure.models.stampseals import StampSeals
from base_structure.models.svkgr import SVKGR
from base_structure.models.svkso import SVKSO
from base_structure.models.eklz import EKLZ

from base_structure.models.organizations import Organizations
from base_structure.models.registrator_models import Registrator_models
from base_structure.models.registrator_model_version import Registrator_model_version
from base_structure.models.years import Year
from base_structure.models.passport_version import Passport_version

class Registrators(models.Model):                                               # Фискальный регистратор. (fiscal registrar)

    modelname = models.ForeignKey(Registrator_models,
                                    verbose_name=u'модель',
                                    null=True,
                                    blank=True)

    version = models.ForeignKey(Registrator_model_version,
                                    verbose_name='версия',
                                    null=True, 
                                    blank=True)


    factorynumber = models.CharField(u'заводской номер',
                                    blank=True,
                                    max_length=255,
                                    unique=True)

    registrnumber = models.CharField(u'регистрационный  номер',                 # Регистрационный номер.
                                    blank=True,
                                    max_length=255)

    stampseals = models.OneToOneField(StampSeals,
                                    verbose_name=u'установленная марка пломба',
                                    null=True,
                                    blank=True)

    svkgr = models.ForeignKey(SVKGR,                                            # идентификатор госреестра. (Visual ID state register)
                                verbose_name=u'идентификатор госреестра(СВКГР)',
                                blank=True, 
                                null=True)

    svkso = models.ForeignKey(SVKSO,                                            # идентификатор сервисного обслуживания. (Visual service ID)
                verbose_name=u'идентификатор сервисного обслуживания(СВКСО)',
                blank=True, 
                null=True)

    eklz  = models.ForeignKey(EKLZ,                                             # Электронная контрольная лента защищенная. (Electronic control tape is protected)
                                verbose_name=u'установленный блок ЭКЛЗ',
                                blank=True, 
                                null=True)

    organization = models.ForeignKey(Organizations,
                                verbose_name='организация',
                                blank=True, 
                                null=True)

    workplace = models.CharField(u'место установки',
                                max_length=255,
                                blank=True)

    year_construction = ForeignKey(Year,
                                verbose_name=u'год выпуска')
                                blank=True, 
                                null=True)
                                
    passport_version_number = ForeignKey(Passport_version,
                                blank=True, 
                                null=True)
    
    def __unicode__(self):
        return u'%s, %s, %s, %s, %s' % (self.factorynumber,
                                        self.modelname,
                                        self.version,
                                        self.registrnumber,
                                        self.organization)

    class Meta:
        app_label = 'base_structure'
        verbose_name_plural = u'регистраторы'
        verbose_name = u'регистратор'
        ordering = ('organization',)


