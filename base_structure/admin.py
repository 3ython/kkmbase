from django.contrib import admin

from base_structure.models.organizations    import Organizations
from base_structure.models.tenders          import Tenders
from base_structure.models.tendertypes      import TenderTypes
from base_structure.models.workers          import Workers
from base_structure.models.eklz             import EKLZ
from base_structure.models.svkso            import SVKSO
from base_structure.models.svkgr            import SVKGR        
from base_structure.models.stampseals       import StampSeals
from base_structure.models.telephonenumbers import TelephoneNumbers

from base_structure.models.registrators     import Registrators
from base_structure.models.registrator_models import Registrator_models
from base_structure.models.registrator_model_version import Registrator_model_version
from base_structure.models.years import Year

from base_structure.models.organizations_ownernames import Organizations_ownernames
from base_structure.models.addresses import Addresses
from base_structure.models.transits import Transits
from base_structure.models.working_times import Working_times
from base_structure.models.individual_nalog_numbers import Individual_nalog_numbers
from base_structure.models.federal_tax_service_inspection_numbers import Federal_tax_service_inspection_numbers
from base_structure.models.workers_status import Workers_status



admin.site.register(Workers)
admin.site.register(TelephoneNumbers)
admin.site.register(Organizations_ownernames)
admin.site.register(Addresses)
admin.site.register(Transits)
admin.site.register(Working_times)
admin.site.register(Individual_nalog_numbers)
admin.site.register(Federal_tax_service_inspection_numbers)
admin.site.register(Workers_status)
admin.site.register(Tenders)
admin.site.register(TenderTypes)
admin.site.register(Organizations)
admin.site.register(SVKSO)
admin.site.register(SVKGR)
admin.site.register(EKLZ)
admin.site.register(StampSeals)

admin.site.register(Registrators)
admin.site.register(Registrator_models)
admin.site.register(Registrator_model_version)
admin.site.register(Year)

# admin.site.register()
