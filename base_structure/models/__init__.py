# coding=utf-8
from django.db import models

from base_structure.models.tenders            import Tenders
from base_structure.models.tendertypes        import TenderTypes

from base_structure.models.organizations      import Organizations
from base_structure.models.workers            import Workers
from base_structure.models.eklz               import EKLZ
from base_structure.models.svkso              import SVKSO
from base_structure.models.svkgr              import SVKGR        
from base_structure.models.stampseals         import StampSeals
from base_structure.models.telephonenumbers   import TelephoneNumbers
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

