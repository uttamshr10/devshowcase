from django.contrib import admin
from django.urls import path, include
from django.conf import settings # accessing settings.py
from django.conf.urls.static import static # create url of static file

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('application.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)   # grab MEDIA_URL and connect it to MEDIA_ROOT
