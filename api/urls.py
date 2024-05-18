from django.urls import path
from api import views

urlpatterns = [
    path('', views.getRoutes, name='routes'),
    path('projects/', views.getProjects, name = 'projects'),
    path('projects/<str:pk>/', views.getProject, name = 'project'),
]