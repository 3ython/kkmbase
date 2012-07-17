# coding= utf-8
from django.db  import models

class EKLZ(models.Model):                                                      # Электронная контрольная лента защищенная. (Electronic control tape is protected)

    registrationNumber = models.CharField(u'регистрационный  номер', 
           
           max_length=13, blank=True, unique=True)


    factoryNumber = models.CharField(u'заводской  номер',       

           max_length=10, blank=True, unique=True)


    activationDate = models.DateField(u'дата  активизации',      

           blank=True, null=True)


    closingDateArchive = models.DateField(u'дата  закрытия архива',  

           blank=True, null=True)


    def __unicode__(self):
        return u'%s,  %s' % (self.registrationNumber, 
                             self.factoryNumber,)
    class Meta:
        verbose_name_plural = u'ЭКЛЗ'

        app_label = 'base_structure'

        verbose_name = u'ЭКЛЗ'
        
        ordering = (u'registrationNumber', 
                    u'factoryNumber', 
                    u'activationDate', 
                    u'closingDateArchive')

