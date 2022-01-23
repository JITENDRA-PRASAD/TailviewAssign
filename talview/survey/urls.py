
from django.urls import path
from . import views

urlpatterns = [
    path('fun1/', views.Surveyview.as_view()),
    path('', views.mainclassview.as_view()),
    path('fun2/',views.Surveyviewfun),
]