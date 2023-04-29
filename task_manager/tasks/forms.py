from django import forms
from django.utils.translation import gettext as tr
from task_manager.tasks.models import Task
from task_manager.statuses.models import TaskStatus
from task_manager.users.models import NewUser


class CreateTaskForm(forms.ModelForm):
    
    class Meta:
        model = Task
        fields = tr("__all__",)

    def __init__(self, *args, **kwqargs):
        super().__init__(*args, **kwqargs)
        self.fields['status'].queryset = TaskStatus.objects.all()
       #  self.fields['user'].queryset = NewUser.objects.all()











# class CreateTaskForm(forms.ModelForm):
#     name = forms.CharField(label=tr('Имя'),
#                            label_suffix='',
#                            max_length=120,
#                            required=True,
#                            widget=forms.TextInput(
#         attrs={'placeholder': tr('Имя'),
#                'class': 'form-control', }))
#     description = forms.Textarea(label=tr('Описание'),
#                            label_suffix='',
#                            max_length=1000,
#                            required=True,
#                            widget=forms.TextInput(
#         attrs={'placeholder': tr('Описание'),
#                'class': 'form-control', }))
#     status = forms.CharField(label=tr('Статус'),
#                            label_suffix='',
#                            max_length=120,
#                            required=True,
#                            widget=forms.TextInput(
#         attrs={'placeholder': tr('Имя'),
#                'class': 'form-control', }))
#     exacutor = forms.CharField(label=tr('Исполнитель'),
#                            label_suffix='',
#                            max_length=120,
#                            required=False,
#                            widget=forms.TextInput(
#         attrs={'placeholder': tr('Исполнитель'),
#                'class': 'form-control', }))
    

#     class Meta:
#         model = Task
#         fields = ('name',)
