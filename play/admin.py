from django.contrib import admin


from .models import *


@admin.register(Play)
class PlayAdmin(admin.ModelAdmin):
    list_display = ('name', 'date')
    

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('name', 'position')


@admin.register(Result)
class ResultAdmin(admin.ModelAdmin):
    list_display = ('employee', 'first', 'second', 'third')


