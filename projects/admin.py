from django.contrib import admin
from projects.models import Project

class ProjectAdmin(admin.ModelAdmin):
    list_display=("title","completed_date")

admin.site.register(Project, ProjectAdmin)

# Register your models here.
