#  coding= utf-8
from django.db  import models

from base_structure.models.years import Year

class SVKSO(models.Model):                #  Визуальный идентификатор сервисного обслуживания. (Visual service ID)
    number = models.CharField(u'номер', 
                         max_length=7, unique=True)

#    year = models.CharField(u'Год', max_length=4)
    
    year = models.ForeignKey(Year,
            verbose_name=u'год', max_length=4)
                
    STATUS = ((u'установлено', u'установлено'), 
           (u'не установлено', u'не установлено'), 
           (u'использовано', u'использовано'))
    
    status = models.CharField(max_length=14,
             verbose_name='статус', choices=STATUS)
    
    def __unicode__(self):
        return u'%s,    %s,    %s' % (self.status,
                                      self.year, 
                                      self.number)
    class Meta:
        verbose_name_plural = u"СВК сервисного обслуживания"
        
        verbose_name = u'СВКСО'
        
        app_label = 'base_structure'
        
        ordering = (u'year',
                    u'number',
                    u'status')
                              