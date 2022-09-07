from django.contrib import admin
from django.urls import path

from . import views 

urlpatterns = [
    path('department/', views.DepartmentListView.as_view(), name='department-list'),
    path('department/create/', views.DepartmentCreateView.as_view(), name='department-create'),
]
