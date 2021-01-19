from django.urls import path

from . import views

app_name = "practice"
urlpatterns = [
    path("", views.index, name="index"),
    path("<int:question_id>", views.details, name="details"),
]
