from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy

from .models import Department


class DepartmentListView(generic.ListView):
    model = Department


class DepartmentCreateView(generic.edit.CreateView):
    model = Department
    fields = ('code', 'name')
    success_url = reverse_lazy('department-list')
