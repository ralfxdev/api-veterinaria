from django.urls import path
from api_veterinaria import views
from django.db import router
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'clientes', views.ClienteView)
router.register(r'personal', views.PersonalView)
router.register(r'animales', views.AnimalView)
router.register(r'diagnosticos', views.DiagnosticoView)
router.register(r'elementos_factura', views.ElementoFacturaView)
router.register(r'facturas', views.FacturaView)

urlpatterns = router.urls

urlpatterns += [
    path('animalespornombre', views.AnimalesNombreList.as_view()),
    path('diagnosticosporfecha', views.DiagnosticoFechaList.as_view()),
    path('diagnosticoanimalpornombre', views.DiagnosticoAnimalNombre.as_view()),
    path('facturaporid', views.FacturaIdList.as_view()),
]

