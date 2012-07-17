# coding= utf-8
from django.db import models

class Federal_tax_service_inspection_numbers(models.Model):
    federal_tax_service_inspection_number = models.CharField(u'номер налоговой инспекции',
                     max_length=255, 
                     unique=True,
                     blank=True)
                     
    def __unicode__(self):
        return u'%s' % (self.Federal_tax_service_inspection_numbers)
    class Meta:
        app_label = 'base_structure'
        verbose_name = u"номер налоговой инспекции"
        verbose_name_plural = u"номера налоговых инспекций"
       #ordering = ('',)
