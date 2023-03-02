from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('weather/', include('weather_app.urls')),
    path('admin/', admin.site.urls),
]
