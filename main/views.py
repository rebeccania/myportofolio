import datetime
from django.contrib import messages
from django.core import serializers
from django.http import HttpResponse
from django.contrib.auth import login,logout
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django.shortcuts import redirect, render
from django.shortcuts import get_object_or_404
from main.forms import ProjectForm,ExperienceForm
from django.contrib.auth.decorators import login_required  # Tambahkan baris ini
from django.core.exceptions import PermissionDenied        # Tambahkan baris ini
from main.models import Experience
from main.models import Education
from main.models import AboutTrait
from main.models import Project

# Create your views here.
def show_main(request):
    last_login = request.COOKIES.get('last_login', 'Belum ada sesi login / Cookie tidak ditemukan')
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
        "last_login": last_login,
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

@login_required(login_url="/login/")
def create_project(request):
    if not request.user.is_superuser:
        raise PermissionDenied

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

def get_projects_json(request):
    title_query = request.GET.get("title", "").strip()
    projects = Project.objects.all()

    if title_query:
        projects = projects.filter(title__icontains=title_query)

    projects_json = serializers.serialize(
        "json", 
        projects, 
        use_natural_foreign_keys=True)
    return HttpResponse(projects_json, content_type="application/json")

@login_required(login_url="/login/")
def delete_project(request, project_id):
    project = get_object_or_404(Project, pk=project_id)

    if not request.user.is_superuser:
            raise PermissionDenied

    if request.method == "POST":
        project.delete()
        messages.success(request, "Project berhasil dihapus!")
        return redirect("main:show_projects")

    return redirect("main:show_projects")

# --- CREATE EXPERIENCE ---
def create_experience(request):
    form = ExperienceForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Pengalaman baru berhasil ditambahkan!")
        return redirect("main:show_experience")

    context = {
        "short_name": "Rebecca",
        "full_name": "Rebeccaniaga Napitupulu",
        "form": form,
    }
    return render(request, "experience_form.html", context)

# --- UPDATE EXPERIENCE ---
def edit_experience(request, id):
    experience = get_object_or_404(Experience, pk=id)
    form = ExperienceForm(request.POST or None, instance=experience)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Pengalaman berhasil diperbarui!")
        return redirect("main:show_experience")

    context = {
        "short_name": "Rebecca",
        "full_name": "Rebeccaniaga Napitupulu",
        "form": form,
    }
    return render(request, "experience_form.html", context)

# --- DELETE EXPERIENCE ---
def delete_experience(request, id):
    experience = get_object_or_404(Experience, pk=id)
    experience.delete()
    messages.success(request, "Pengalaman berhasil dihapus!")
    return redirect("main:show_experience")

# --- JSON DATA DELIVERY ---
def get_experience_json(request):
    experience_list = Experience.objects.all()
    experience_json = serializers.serialize("json", experience_list)
    return HttpResponse(experience_json, content_type="application/json")

def login_user(request):
    form = AuthenticationForm(request, data=request.POST or None)

    if request.method == "POST" and form.is_valid():
        user = form.get_user()
        login(request, user)
        response = redirect("main:show_main")
        response.set_cookie('last_login', datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        return response

    context = {
        "name": "Rebeccaniaga Napitupulu",
        "form": form,
    }
    return render(request, "login.html", context)

def register(request):
    form = UserCreationForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Akun berhasil dibuat. Silakan login.")
        return redirect("main:login")

    context = {
        "name": "Rebeccaniaga Napitupulu",
        "form": form,
    }
    return render(request, "register.html", context)

def logout_user(request):
    logout(request)
    return redirect("main:show_main")

# Tanpa cek is_superuser: semua akun yang sudah login boleh memberi star
@login_required(login_url="/login/")
def toggle_star(request, project_id):
    project = get_object_or_404(Project, pk=project_id)

    if request.method == "POST":
        # Kalau akun ini sudah pernah memberi star, batalkan star-nya.
        # Kalau belum, tambahkan star.
        if request.user in project.starred_by.all():
            project.starred_by.remove(request.user)
        else:
            project.starred_by.add(request.user)

    return redirect("main:show_projects")