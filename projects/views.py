from django.shortcuts import render
from .models import Project


def project_list(request):
    projects = Project.objects.all()
    context = {
        'projects': projects
    }
    return render(request, 'projects/index.html', context)


def full_view(request, pk):
    project = Project.objects.get(pk=pk)
    context = {
        'project': project
    }
    return render(request, 'projects/full_view.html', context)
