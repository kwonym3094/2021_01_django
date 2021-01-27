from django.urls import path
from . import views

app_name = "api_user"

urlpatterns = [
    path("", views.UserView.as_view(), name="userview"),
    path("<int:user_id>/", views.UserView.as_view()),  # User pk id가 전달되는 경우
]
