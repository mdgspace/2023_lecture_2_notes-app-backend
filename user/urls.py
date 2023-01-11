from django.contrib import admin
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('signin/',views.UserSiginView.as_view()),
    path('signup/',views.UserSignupView.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)