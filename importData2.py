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

#OrganizationsList = pickle.load(file('../kkmbase_copy2/OrganizationsList.pickle'))
OrganizationsList = pickle.load(file('OrganizationsList.pickle'))


def main():
    for c in OrganizationsList:
        if not c['ownername'] == '':
            org_name = Organizations_ownernames(ownername=c['ownername'])
            org_name.save()
        if not c['address'] == '':
            org_address = Addresses(address=c['address'])
            org_address.save()
        if not c['telephonenumber'] == '':
            org_telephone = TelephoneNumbers(phonenumber = c['telephonenumber'])
            org_telephone.save
        if not c['transit'] == '':
            org_transit = Transits(transit=c['transit'])
            org_transit.save()
        if not c['working_time'] == '':
            org_worktime = Working_times(working_time = c['working_time'])
            org_worktime.save()
        if not c['inn'] == '':
            org_inn = Individual_nalog_numbers(inn=c['inn'])
            org_inn.save()
        if not c['federal_tax_service_inspection_number'] == '':
            org_inspectnumber = Federal_tax_service_inspection_numbers(federal_tax_service_inspection_number = c['federal_tax_service_inspection_number'])
            org_inspectnumber.save()
            
        # o.workers = c['workers']