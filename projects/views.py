from django.shortcuts import render
from projects.models import Project

def project_index(request):
    projects = Project.objects.all()  # Get all projects
    context = {
        "projects": projects  # Pass all projects to the template
    }
    return render(request, "projects/project_index.html", context)  # Render the index template

def project_detail(request, pk):
    project = Project.objects.get(pk=pk)  # Get a specific project by pk
    context = {
        "project": project  # Pass the project to the detail template
    }
    return render(request, "projects/project_detail.html", context)  # Render the detail template
