from django.contrib import admin
from api_veterinaria import models

# Register your models here.

admin.site.register(models.Cliente)
admin.site.register(models.Personal)
admin.site.register(models.Animal)
admin.site.register(models.Diagnostico)
admin.site.register(models.ElementoFactura)
admin.site.register(models.Factura)
