from django.contrib import admin
from .models import TblCategoria, TblCurso  # Usa .models si está en la misma app

# Registrar modelos correctamente
admin.site.register(TblCategoria)
admin.site.register(TblCurso)
