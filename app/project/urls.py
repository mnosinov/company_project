from django.contrib import admin
from django.urls import path, include
from django.views import generic


urlpatterns = [
    path('', generic.TemplateView.as_view(template_name="index.html")),
    path('', include('company.urls')),
    path('admin/', admin.site.urls),
]
