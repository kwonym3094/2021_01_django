from django.urls import path

from . import views

app_name = "pybo"
urlpatterns = [
    path("", views.index, name="index"),
    path("<int:question_id>/", views.details, name="details"),
    path("answer/create/<int:question_id>/", views.answer_create, name="answer_create"),
    # generic view를 사용할 경우
    # path("", views.IndexView.as_view()),
    # path("<int:pk>/", views.DetailView.as_view()),
]
