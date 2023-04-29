from django.views.generic import TemplateView, CreateView, UpdateView, DeleteView, DetailView
from django.utils.translation import gettext_lazy as tr
from task_manager.tasks.forms import CreateTaskForm
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib import messages

class TasksView(TemplateView):
    template_name = 'tasks.html'



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