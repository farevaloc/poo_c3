from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('aichat/', include('aichat.urls')),
    path('', RedirectView.as_view(url='/aichat/login/', permanent=True)),
]
