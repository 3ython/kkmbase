# coding= utf-8
from django.db import models

from base_structure.models.organizations import Organizations
from base_structure.models.registrators  import Registrators
from base_structure.models.stampseals    import StampSeals
from base_structure.models.svkgr         import SVKGR
from base_structure.models.svkso         import SVKSO
from base_structure.models.eklz          import EKLZ
from base_structure.models.tendertypes   import TenderTypes

class Tenders(models.Model):                              # Заявка. (tenders)

    STATUS = ((u'выполнена', u'выполнена'), 
              (u'не выполнена', u'не выполнена'))
    
    status = models.CharField(max_length=255,
          verbose_name='Статус (состояние) заявки', 
                              choices=STATUS)

    number = models.CharField(u'номер заявки',
               max_length=255, unique=True)        # Номер заявки.
                                           
    date = models.DateField(u'дата от', 
               blank=True, null=True)
    
    organization = models.ForeignKey(Organizations,
                       blank=True, null=True)
    
    registrator = models.ForeignKey(Registrators,
                      verbose_name='ККМ',
                      blank=True, null=True)
    
    stampseals = models.ForeignKey(StampSeals,
                      verbose_name='марка пломба',
                      blank=True, null=True)
    
    svkgr = models.ForeignKey(SVKGR,               # идентификатор госреестра. (Visual ID state register)
                              verbose_name='СВКГР',
                              blank=True, null=True)
                     
    svkso = models.ForeignKey(SVKSO,               # идентификатор сервисного обслуживания. (Visual service ID)
                              verbose_name='СВКСО',   
                              blank=True, null=True)
    
    eklz = models.ForeignKey(EKLZ,                 # Электронная контрольная лента защищенная. (Electronic control tape is protected)
                             verbose_name='ЭКЛЗ',                      
                             blank=True, null=True)
                      
    workaccomplished = models.CharField(u'выполненная работа',        # Выполненная работа. 
                        max_length=200, blank=True)
                                           
    asserteddefect = models.CharField(u'заявленная неисправность',    # Заявленная неисправность.
                        max_length=255, blank=True)
                                           
    faultdetected = models.CharField(u'выявленная неисправность',     # Выявленная неисправность.
                        max_length=255, blank=True)

    usedspareparts = models.CharField(u'использованные запчасти',     # Использованные запчасти, материалы. 
                        max_length=255, blank=True)

    tendertypes = models.ManyToManyField(TenderTypes,
                       verbose_name='тип (вид) заявки',
                       blank=True, null=True)
    
    def __unicode__(self): 
        return u'%s, %s' % (self.number, self.date)

    class Meta:
        verbose_name_plural = u"заявки"

        app_label           = 'base_structure'

        verbose_name        = u"заявка"        
       #ordering = ('',)



