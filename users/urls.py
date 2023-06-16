from django.urls import path
from users import views


urlpatterns = [
    path('', views.Profile, name= 'profiles'),
    path('profile/<str:pk>/', views.userProfile, name = 'user-profile'),
]
