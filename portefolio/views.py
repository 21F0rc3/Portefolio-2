from multiprocessing import context
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import Project

from controllers.fileController import *

# Create your views here.
def index(request):
    template = loader.get_template('portefolio/index.html')
    
    projects = Project.objects.select_related('logo_image').all()

    context = {
        'projects': projects
    }

    return HttpResponse(template.render(context, request))

def seeProjectDetails(request):
    this_project = Project.objects.filter(name=request.project_name).first()

    project_sections = getProjectSections(this_project.id)

    return render_template("/layouts/project.html", project=readProject(this_project), sections=project_sections)