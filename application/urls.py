from django.urls import path
from . import views

urlpatterns=[
    path("projects/", views.projects, name="projects"),
    path("project/<str:pk>/", views.project, name="project"),
    path("create-project/", views.createProject, name = "create"),
    path("update-project/<str:pk>/", views.updateProject, name = 'update'),
    path("delete-project/<str:pk>/", views.deleteProject, name = 'delete'),

    # CRUD OPERATION WITH GENERIC VIEWS.
    # path("create-project", views.CreateProject.as_view(), name = 'create'),
    # path("projects/", views.ListProject.as_view(), name='projects'),
    # path("project/<str:pk>/", views.DetailProject.as_view(), name = 'project'),
    # path("update-project/<str:pk>/", views.UpdateProject.as_view(), name='update'),
    # path("delete-project/<str:pk>/", views.DeleteProject.as_view(), name = 'delete'),
]
