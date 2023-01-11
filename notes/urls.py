from django.contrib import admin
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('<int:id>',views.UserNoteView.as_view()),
    path('<str:username>',views.UserNotesView.as_view()),
    path('',views.UserNoteView.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)