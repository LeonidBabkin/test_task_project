from django.contrib.auth import authenticate
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as tr
from django.forms import ModelForm
from django import forms


class LoginUserForm(ModelForm):

    username = forms.CharField(label=tr('Имя пользователя'),
                               max_length=20,
                               label_suffix='',
                               required=True,
                               help_text=tr('Введите логин'),
                               widget=forms.TextInput(
        attrs={'placeholder': tr('Имя пользователя'),
               'autofocus': True,
               'class': 'form-control', }),
        error_messages={'unique': tr(
            'Пользователь с таким именем'
            ' уже есть')})
    password = forms.CharField(label=tr('Пароль'),
                               label_suffix='',
                               max_length=100,
                               required=True,
                               help_text=tr("введите пароль"),
                               widget=forms.PasswordInput(
        attrs={'placeholder': tr('Пароль'),
                               'class': 'form-control', }))

    class Meta:
        model = get_user_model()
        fields = ('username', 'password')

    def clean(self):
        if self.is_valid():
            username = self.cleaned_data['username']
            password = self.cleaned_data['password']
            if not authenticate(username=username, password=password):
                raise forms.ValidationError(
                    'Неверное имя пользователя или пароль')