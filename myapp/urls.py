from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("", views.home,name="home"),
    path("candidate_register/", views.candidate_register,name="candidate_register"),
    path("organization/", views.organization,name="organization"),
    path("organization_signup/", views.organization_signup,name="organization_signup"),
    path("organization_signin/", views.organization_signin,name="organization_signin"),
]