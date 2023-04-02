from django.contrib import admin
from AppCoder.models import Plan_Medicina_Deportiva, Plan_Kinesiologia_Fisioterapia, Plan_Nutricion, Plan_Preparacion_Fisica, Plan_Psicologia_Deportiva

# Register your models here.
admin.site.register(Plan_Medicina_Deportiva)
admin.site.register(Plan_Kinesiologia_Fisioterapia)
admin.site.register(Plan_Nutricion)
admin.site.register(Plan_Preparacion_Fisica)
admin.site.register(Plan_Psicologia_Deportiva)
