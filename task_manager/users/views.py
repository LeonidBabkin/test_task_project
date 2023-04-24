# from django.contrib.auth import authenticate, login, logout
# from django.utils.translation import gettext_lazy as tr
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.urls import reverse_lazy
from django.contrib import messages
from django.views import View
from . import forms


class Index(TemplateView):

    template_name = 'index.html'


class UserRegisterView(View):
    def get(self, request, *args, **kwargs):
        context = {}
        form = forms.CreateUserForm()
        context['registration_form'] = form
        return render(request, 'users/register.html', context)

    def post(self, request, *args, **kwargs):
        context = {}
        form = forms.CreateUserForm(request.POST)
        if form.is_valid():  # Если данные корректные, то сохраняем данные формы
            form.save()
            messages.success(request, "Пользователь зарегистрирован")

            # переделать redirect позже на login
            return redirect(reverse_lazy('login'))  # Редирект на указанный маршрут
        messages.error(request, 'Ошибка в регистрации. Попробуйте снова')
        context['registration_form'] = form
        return render(request, 'users/register.html', context)
