from django.contrib import admin
from apps.models import Project
@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    pass

