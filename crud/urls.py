from django.conf.urls import url, include
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^sosmed/', include('sosmed.urls', namespace='sosmed')),
    url(r'^$', views.index),
    url(r'^admin/', admin.site.urls),
]
