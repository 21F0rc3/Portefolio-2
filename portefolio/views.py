from multiprocessing import context
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import Project

# Create your views here.
def index(request):
    template = loader.get_template('portefolio/index.html')
    
    projects = Project.objects.select_related('logo_image').all()

    context = {
        'projects': projects
    }

    return HttpResponse(template.render(context, request))