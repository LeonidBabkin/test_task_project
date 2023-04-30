from django.views.generic import TemplateView, CreateView, UpdateView, DeleteView, DetailView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.utils.translation import gettext_lazy as tr
from task_manager.tasks.forms import CreateTaskForm, ShowTasksForm
from django.shortcuts import render, redirect
from task_manager.tasks.models import Task
from django.urls import reverse_lazy
from django.contrib import messages


# @method_decorator(login_required, name='dispatch')
class TasksView(TemplateView):

    def get(self, request, *args, **kwargs):
        form = ShowTasksForm()
        context = {
                'tasks': Task.objects.all().order_by('id'),
                'form': form
            }
        return render(request, 'tasks.html', context)


# @method_decorator(login_required, name='dispatch')
class TaskCreateView(CreateView):

    def get(self, request, *args, **kwargs):
        form = CreateTaskForm()
        return render(request, 'tasks/create_task.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form = CreateTaskForm(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request, tr('Задание успешно создано'))
            return redirect(reverse_lazy('home'))
        else:
            return render(request, 'tasks/create_task.html', {'form': form})