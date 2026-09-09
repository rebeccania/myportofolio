from django.shortcuts import render

from main.models import Experience

# Create your views here.
def show_main(request):
    context = {
        "name": "Rebeccaniaga Napitupulu",
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
        "name": "Rebecca",
        "experience_list": Experience.objects.all(),
    }
    return render(request, "experience.html", context)