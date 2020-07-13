from django.urls import path
from . import views

urlpatterns = [
    path('', view = views.home, name = 'home'),
    path('cpidata/', view = views.get_cpidata_api, name = 'cpi_data_api'),
    path('ppidata/', view = views.get_ppidata_api, name = 'ppi_data_api'),
    path('cpippi/', view = views.get_cpippi_api, name = 'cpi_ppi_data_api'),
]