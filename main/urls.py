from django.urls import path

from main.views import show_about, show_main, show_experience, show_education, create_project, show_projects,show_projects,get_projects_json, delete_project,create_experience, edit_experience, delete_experience, get_experience_json, register, login_user, logout_user, toggle_star

app_name = "main"

urlpatterns = [
    path("", show_main, name="show_main"),
    path("experience/", show_experience, name="show_experience"),
    path("education/", show_education, name="show_education"),
    path('about/', show_about, name='show_about'),
    path("projects/add/", create_project, name="create_project"),
    path("projects/", show_projects, name="show_projects"),
    path("api/projects/", get_projects_json, name="get_projects_json"),
    path("projects/<uuid:project_id>/delete/", delete_project, name="delete_project"),
    path("experience/add/", create_experience, name="create_experience"),
    path("experience/edit/<uuid:id>/", edit_experience, name="edit_experience"),
    path("experience/delete/<uuid:id>/", delete_experience, name="delete_experience"),
    path("api/experience/", get_experience_json, name="get_experience_json"),
    path("register/", register, name="register"),
    path("login/", login_user, name="login"),
    path("logout/", logout_user, name="logout"),
    path("projects/<uuid:project_id>/star/",toggle_star,name="toggle_star",
),
]