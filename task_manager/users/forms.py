# from django.contrib.auth import authenticate
# from django.contrib.auth import get_user_model
# from django.utils.translation import gettext_lazy as tr
from django.contrib.auth.forms import UserCreationForm
# from django.forms import ModelForm
from .models import NewUser
from django import forms


class CreateUserForm(UserCreationForm):
    class Meta:
        model = NewUser
        fields = ['first_name',
                  'last_name',
                  'username',
                  'password1',
                  'password2',
                  ]

        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'John'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Smith'}),
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'John_Redneck'}),
        }
        #     'password1': forms.PasswordInput(attrs={'placeholder': 'Not less than 8 characters'}),
        #     'password2': forms.PasswordInput(attrs={'placeholder': 'Re-enter Password: not fewer than 8 characters '}),
        # }

    def __init__(self, *args, **kwargs):
        super(CreateUserForm, self).__init__(*args, **kwargs)
        self.fields['password1'].widget = forms.PasswordInput(
            attrs={'class': 'form-control', 'placeholder': 'Password from numbers and letters of the Latin alphabet'})
        self.fields['password2'].widget = forms.PasswordInput(
            attrs={'class': 'form-control', 'placeholder': 'Password confirmation'})