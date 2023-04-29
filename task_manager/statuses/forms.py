from django import forms
from django.utils.translation import gettext as tr
from task_manager.statuses.models import TaskStatus


class CreateStatusForm(forms.ModelForm):
    name = forms.CharField(label=tr('Имя'),
                           label_suffix='',
                           max_length=120,
                           required=True,
                           widget=forms.TextInput(
        attrs={'placeholder': tr('Имя'),
               'class': 'form-control', }))

    class Meta:
        model = TaskStatus
        fields = ('name',)


class UpdateStatusForm(forms.ModelForm):
    name = forms.CharField(label=tr('Имя'),
                           label_suffix='',
                           max_length=120,
                           required=True,
                           widget=forms.TextInput(
        attrs={'placeholder': tr('Имя'),
               'class': 'form-control', }))

    class Meta:
        model = TaskStatus
        fields = ('name',)
