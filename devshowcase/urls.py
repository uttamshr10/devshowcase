from django.contrib import admin
from django.urls import path, include
from django.conf import settings # accessing settings.py
from django.conf.urls.static import static # create url of static file
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('projects/', include('application.urls')),
    path('', include('users.urls')),
    # User submits email for reset
    path('reset_password/', auth_views.PasswordResetView.as_view(template_name = 'auth/reset_password.html'), name = 'reset_password'),
    # Reset email sent to the user
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name = 'auth/password_reset_done.html'), name = 'password_reset_done'),
    # Email with link and reset instructions in the mailbox.
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name = 'auth/password_reset_confirm.html'), name = 'password_reset_confirm'),
    # Password is successfully changed.
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name='auth/password_reset_complete.html'), name = 'password_reset_complete'),
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)   # grab MEDIA_URL and connect it to MEDIA_ROOT
urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT) # grab STATIC_URL and connect it to STATIC_ROOT on production
