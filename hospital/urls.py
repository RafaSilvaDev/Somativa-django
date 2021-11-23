from django.contrib import admin
from django.urls import path, include
from home import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.index, name='index'),
    path('admin/', admin.site.urls),
    path('user/', include('paciente.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)