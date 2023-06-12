from django.contrib import admin
from django.urls import path, include
from django.conf import settings # accessing settings.py
from django.conf.urls.static import static # create url of static file

urlpatterns = [
    path('admin/', admin.site.urls),
    path('projects/', include('application.urls')),
    path('', include('users.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)   # grab MEDIA_URL and connect it to MEDIA_ROOT
urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT) # grab STATIC_URL and connect it to STATIC_ROOT on production
