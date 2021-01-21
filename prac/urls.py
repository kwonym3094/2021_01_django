from django.urls import path
from . import views

app_name = "prac"
urlpatterns = [
    path("", views.index, name="index"),
    path("<int:question_id>/", views.details, name="details"),
    path("create/answer/<int:question_id>/", views.answer_create, name="answer_create"),
    path("create/question/", views.question_create, name="question_create"),
]
