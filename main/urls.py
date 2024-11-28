from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("info/<str:inn>/", views.org_info, name="org_info"),
]
