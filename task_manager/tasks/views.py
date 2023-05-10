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
# class TaskCreateView(CreateView):

#     def get(self, request, *args, **kwargs):
#         form = CreateTaskForm()
#         return render(request, 'tasks/create_task.html', {'form': form})

#     def post(self, request, *args, **kwargs):
#         form = CreateTaskForm(request.POST)
#         if form.is_valid():
# # That's useful when you get most of your model data from a form, but you need to populate
# # some null=False fields with non-form data.Saving with commit=False gets you a model object,
# # then you can add your extra data and save it.
#             post = form.save(commit=False)
#             # fill in the field author with with current user id
#             post.author = NewUser.objects.get(id=request.user.id)
#             post.save()
#             messages.info(request, tr('Задача успешно создана'))
#             return redirect('tasks')
#         else:
#             return render(request, 'tasks/create_task.html', {'form': form})
