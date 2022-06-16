from django.db import models

# Create your models here.

class Project(models.Model):
    name = models.CharField(max_length=200)
    #logo_file_id = models.Column(models.Integer, models.ForeignKey('project.id'))
    description = models.CharField(max_length=500, null=True)
    keywords = models.CharField(max_length=500, null=True)

    def __str__(self):
        return self.name