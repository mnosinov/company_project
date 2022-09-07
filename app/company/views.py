from django.shortcuts import render
from django.views import generic, View
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect

from .models import Department
from .forms import DepartmentForm


class DepartmentListView(generic.ListView):
    model = Department


class DepartmentCreateView(generic.edit.CreateView):
    model = Department
    fields = ('id', 'code', 'name')
    success_url = reverse_lazy('department-list')


class DepartmentManuallyCreateView(View):
    template_name = 'company/department_form_manually.html'
    form_class = DepartmentForm

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            if False:    # folk for 2 variants of saving
                form.save()
            else:
                Department.objects.create(
                    id=request.POST['id'],
                    code=request.POST['code'],
                    name=request.POST['name']
                )
            return HttpResponseRedirect(reverse_lazy('department-list'))
        return render(request, self.template_name, {'form': form})

