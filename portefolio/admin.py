from django.contrib import admin

from .models import Project, Image, File, Section

# Register your models here.
admin.site.register(Project)
admin.site.register(Image)
admin.site.register(File)
admin.site.register(Section)