from django.conf.urls import url, include
from app.municipio.views import MunicipioList, MunicipioCreate, MunicipioUpdate, MunicipioDelete



urlpatterns = [
    url(r'^nuevo$', MunicipioCreate.as_view(), name='municipio_crear'),
    url(r'^listar$', MunicipioList.as_view(), name='municipio_listar'),
    url(r'^editar/(?P<pk>\d+)/$', MunicipioUpdate.as_view(), name='municipio_editar'),
    url(r'^eliminar/(?P<pk>\d+)/$', MunicipioDelete.as_view(), name='municipio_eliminar'),

]
