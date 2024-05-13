from django.urls import path
from users import views


urlpatterns = [
    path('', views.Profile, name= 'profiles'),
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutPage, name = 'logout'),
    path('register/', views.registerPage, name='register'),
    path('profile/<str:pk>/', views.userProfile, name = 'user-profile'),
    path('account/', views.userAccount, name = 'account'),
    path('edit-account/', views.editAccount, name = 'edit-account'),
    path('create-skill/', views.createSkill, name='create-skill'),
    path('update-skill/<str:pk>/', views.updateSkill, name='update-skill'),
    path('delete-skill/<str:pk>/', views.deleteSkill, name='delete-skill'),
]
