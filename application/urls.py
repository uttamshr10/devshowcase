from django.urls import path
from . import views

urlpatterns=[
    # urls for function based views
    path("", views.projects, name="projects"),    # list view
    path("project/<str:pk>/", views.project, name="project"),   # detail view 
    path("create-project/", views.createProject, name = "create"),   # create view
    path("update-project/<str:pk>/", views.updateProject, name = 'update'),  # update view
    path("delete-project/<str:pk>/", views.deleteProject, name = 'delete'),  # delete view

    # CRUD OPERATION WITH GENERIC VIEWS.
    # path("create-project", views.CreateProject.as_view(), name = 'create'),
    # path("projects/", views.ListProject.as_view(), name='projects'),
    # path("project/<str:pk>/", views.DetailProject.as_view(), name = 'project'),
    # path("update-project/<str:pk>/", views.UpdateProject.as_view(), name='update'),
    # path("delete-project/<str:pk>/", views.DeleteProject.as_view(), name = 'delete'),
]
