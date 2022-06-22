from distutils.command.upload import upload
from django.db import models

# Create your models here.

class Image(models.Model):
    image_file = models.ImageField(upload_to='images')

class Project(models.Model):
    name = models.CharField(max_length=200)
    logo_image = models.OneToOneField(Image, on_delete=models.SET_NULL, null=True)
    description = models.CharField(max_length=500, null=True)
    keywords = models.CharField(max_length=500, null=True)

    def __str__(self):
        return self.name

class File(models.Model):
    file = models.FileField(upload_to='files')

class Section(models.Model):
    title = models.CharField(max_length=50)
    image_file = models.OneToOneField(Image, on_delete=models.SET_NULL, null=True)
    content_file = models.OneToOneField(File, on_delete=models.SET_NULL, null=True)
    project = models.OneToOneField(Project, on_delete=models.SET_NULL, null=True)