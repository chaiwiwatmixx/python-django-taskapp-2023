from django.contrib import admin
from taskapp.models import Task

class TaskAdmin(admin.ModelAdmin):
    list_display=["name","status"]

# Register your models here.
admin.site.register(Task,TaskAdmin)
