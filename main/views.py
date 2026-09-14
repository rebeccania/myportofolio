from django.contrib import messages
from django.shortcuts import redirect, render
from main.forms import ProjectForm

from main.models import Experience
from main.models import Education
from main.models import AboutTrait
from main.models import Project

# Create your views here.
def show_main(request):
    context = {
        "name": "Rebeccaniaga Napitupulu",
        'short_name': "Rebecca",
        "full_name": "Rebeccaniaga Napitupulu",
        "npm": "2506598394",
        "study_program": "S1 Sistem Informasi",
        "bio": (
            "Information Systems student at the Faculty of Computer Science, Universitas Indonesia, currently in my third semester. "
            "I'm interested in Product, Data, and Marketing, and passionate about exploring how technology and data can be turned into meaningful solutions."
            " I'm always eager to learn, grow, and build impactful IT solutions for the future."
        ),
    }
    return render(request, "index.html", context)


def show_experience(request):
    context = {
        'short_name': "Rebecca",
        "full_name": "Rebeccaniaga Napitupulu",
        "experience_list": Experience.objects.all(),
    }
    return render(request, "experience.html", context)

def show_education(request):
    education_list = Education.objects.all().order_by('-start_year')
    context = {
        'short_name': "Rebecca",
        'full_name': 'Rebeccaniaga Napitupulu',
        'education_list': education_list,
    }
    return render(request, 'education.html', context)

def show_about(request):
    traits = AboutTrait.objects.all()
    context = {
        'short_name': 'Rebecca',
        'full_name': 'Rebeccaniaga Napitupulu',
        'traits': traits,
    }
    return render(request, 'about.html', context)

def create_project(request):
    form = ProjectForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Proyek baru berhasil ditambahkan!")
        return redirect("main:show_projects")

    context = {
        "short_name": "Rebecca",
        "full_name": "Rebeccaniaga Napitupulu",
        "form": form,
    }
    return render(request, "projects_form.html", context)

def show_projects(request):
    context = {
        "short_name": "Rebecca",
        "full_name": "Rebeccaniaga Napitupulu",
        "project_list": Project.objects.all(),
    }
    return render(request, "project.html", context)