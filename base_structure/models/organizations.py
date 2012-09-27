# coding= utf-8
from django.db import models
from base_structure.models.telephonenumbers import TelephoneNumbers
from base_structure.models.workers import Workers
from base_structure.models.organizations_ownernames import Organizations_ownernames
from base_structure.models.addresses import Addresses
from base_structure.models.transits import Transits
from base_structure.models.working_times import Working_times
from base_structure.models.individual_nalog_numbers import Individual_nalog_numbers
from base_structure.models.federal_tax_service_inspection_numbers import Federal_tax_service_inspection_numbers


class Organizations(models.Model):

    ownername = models.ForeignKey(Organizations_ownernames,
                             verbose_name=u'название организации',
                             blank=True,
                             null=True)

    address = models.ForeignKey(Addresses,
                    verbose_name=u'адрес',
                    blank=True,
                    null=True)

    telephonenumber = models.ManyToManyField(TelephoneNumbers,
                        verbose_name=u'телефон',
                        max_length=255,
                        blank=True,
                        null=True)

    workers = models.ManyToManyField(Workers,
                  verbose_name=u'сотрудники',
                  blank=True,
                  null=True)

    transit = models.ManyToManyField(Transits,
                     verbose_name=u'проезд',
                     max_length=255,
                     blank=True,
                     null=True)

    working_time = models.ForeignKey(Working_times,
                verbose_name=u'часы работы',
                blank=True,
                null=True)

    inn = models.ForeignKey(Individual_nalog_numbers,
                        verbose_name=u'ИНН',
                        blank=True,
                        null=True)

    federal_tax_service_inspection_number = models.ForeignKey(Federal_tax_service_inspection_numbers,
                      verbose_name=u'№ ИФНС',
                      max_length=10,
                      blank=True,
                      null=True)

    def __unicode__(self):
        return u'%s, %s, ИФНС №%s' % (self.address,
                                      self.ownername,
                                      self.federal_tax_service_inspection_number)

    class Meta:

        app_label = 'base_structure'
        verbose_name = u'организация'
        verbose_name_plural = u'организации'
        ordering = ('address',)
