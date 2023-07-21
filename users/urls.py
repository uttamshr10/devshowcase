from django.urls import path
from users import views


urlpatterns = [
    path('', views.Profile, name= 'profiles'),
    path('register/', views.loginPage, name='register'),
    path('logout/', views.logoutPage, name = 'logout'),
    path('profile/<str:pk>/', views.userProfile, name = 'user-profile'),
]
