# coding= utf-8

import pickle

from base_structure.models.tenders import Tenders
from base_structure.models.tendertypes import TenderTypes
from base_structure.models.organizations import Organizations
from base_structure.models.workers import Workers
from base_structure.models.eklz import EKLZ
from base_structure.models.svkso import SVKSO
from base_structure.models.svkgr import SVKGR
from base_structure.models.stampseals import StampSeals
from base_structure.models.telephonenumbers import TelephoneNumbers
from base_structure.models.years import Year
from base_structure.models.registrators import Registrators
from base_structure.models.registrator_models import Registrator_models
from base_structure.models.registrator_model_version import Registrator_model_version
from base_structure.models.organizations_ownernames import Organizations_ownernames
from base_structure.models.addresses import Addresses
from base_structure.models.transits import Transits
from base_structure.models.working_times import Working_times
from base_structure.models.individual_nalog_numbers import Individual_nalog_numbers
from base_structure.models.federal_tax_service_inspection_numbers import Federal_tax_service_inspection_numbers
from base_structure.models.workers_status import Workers_status

OrganizationsList = pickle.load(file('OrganizationsList.pickle'))


def main():
    for c in OrganizationsList:
        print 'ownername:', c['ownername']
        if Organizations_ownernames.objects.filter(ownername=c['ownername']):
            org_name = Organizations_ownernames.objects.get(ownername=c['ownername'])
        else:
            org_name = Organizations_ownernames(ownername=c['ownername'])
            org_name.save()

        print 'address:', c['address']
        if Addresses.objects.filter(address=c['address']):
            org_address = Addresses.objects.get(address=c['address'])
        else:
            org_address = Addresses(address=c['address'])
            org_address.save()

        print 'telephonenumber:', c['telephonenumber']
        if TelephoneNumbers.objects.filter(phonenumber=c['telephonenumber']):
            org_telephone = TelephoneNumbers.objects.get(phonenumber=c['telephonenumber'])
        else:
            org_telephone = TelephoneNumbers(phonenumber=c['telephonenumber'])
            org_telephone.save()

        print 'transit:', c['transit']
        if Transits.objects.filter(transit=c['transit']):
            org_transit = Transits.objects.get(transit=c['transit'])
        else:
            org_transit = Transits(transit=c['transit'])
            org_transit.save()

        print 'working_time:', c['working_time']
        if Working_times.objects.filter(working_time=c['working_time']):
            org_worktime = Working_times.objects.get(working_time=c['working_time'])
        else:
            org_worktime = Working_times(working_time=c['working_time'])
            org_worktime.save()

        print 'inn:', c['inn']
        if Individual_nalog_numbers.objects.filter(inn=c['inn']):
            org_inn = Individual_nalog_numbers.objects.get(inn=c['inn'])
        else:
            org_inn = Individual_nalog_numbers(inn=c['inn'])
            org_inn.save()

        print 'inspection_number:', c['federal_tax_service_inspection_number']
        if Federal_tax_service_inspection_numbers.objects.filter(federal_tax_service_inspection_number=c['federal_tax_service_inspection_number']):
            org_inspectnumber = Federal_tax_service_inspection_numbers.objects.get(federal_tax_service_inspection_number=c['federal_tax_service_inspection_number'])
        else:
            org_inspectnumber = Federal_tax_service_inspection_numbers(federal_tax_service_inspection_number = c['federal_tax_service_inspection_number'])
            org_inspectnumber.save()

        # o.workers = c['workers']
        print '_______________________'
