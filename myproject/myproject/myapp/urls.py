from django.urls import path
from . import views

urlpatterns = [
    path('', view = views.home, name = 'home'),
    path('cpiyoy/', view = views.get_cpi_yoy, name = 'cpi_forecast'),
    path('ppiyoy/', view = views.get_ppi_yoy, name = 'ppi_forecast'),
    path('cpimom/', view = views.get_cpi_mom, name = 'cpi_mom'),
    path('ppimom/', view = views.get_ppi_mom, name = 'ppi_mom'),
    path('cpidata/', view = views.get_cpidata_api, name = 'cpi_data_api'),
    path('ppidata/', view = views.get_ppidata_api, name = 'ppi_data_api'),
    path('cpicompare/', view = views.get_cpi_compare, name = 'cpi_compare'),
    path('ppicompare/', view = views.get_ppi_compare, name = 'ppi_compare')

]