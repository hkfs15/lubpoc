from django.contrib import admin

from .models import Make, LubMake, Series, Engine, Car, Lub
# Register your models here.


class MakeAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ('name', 'website', 'last_modified')


class LubMakerAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ('name', 'website', 'last_modified')


class SeriesAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ('name', 'make', 'last_modified')


class EngineAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('model',)}
    list_display = ('model', 'brand', 'series', 'last_modified')


class CarAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('model',)}
    list_display = ('model', 'series', 'year', 'lub_type', 'motor_type', 'last_modified')


class LubAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ('name', 'lubmake', 'lub_type', 'motor_type', 'sae_grade',
                    'density', 'viscosity_40', 'pourpoint', 'last_modified')

admin.site.register(Make, MakeAdmin)
admin.site.register(LubMake, LubMakerAdmin)
admin.site.register(Series, SeriesAdmin)
admin.site.register(Engine, EngineAdmin)
admin.site.register(Car, CarAdmin)
admin.site.register(Lub, LubAdmin)
