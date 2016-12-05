# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from django.contrib.auth import logout as django_logout, authenticate, login as django_login
from django.views import View

from users.forms import LoginForm


class LoginView(View):

    @staticmethod
    def get(request):
        form = LoginForm()
        context = {
            'errors': ' ',
            'login_form': form
        }
        return render(request, 'users/login.html', context)

    @staticmethod
    def post(request):
        error_messages = []
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('usr')
            password = form.cleaned_data.get('pwd')
            user = authenticate(username=username, password=password)
            if user is None:
                error_messages.append('Nombre de usuario o contraseña incorrectos.')
            else:
                if user.is_active:
                    django_login(request, user)
                    url = request.GET.get('next', 'photos_home')
                    return redirect(url)
                else:
                    error_messages.append('El usuario no está activo.')

        context = {
            'errors': error_messages,
            'login_form': form
        }
        return render(request, 'users/login.html', context)


class LogoutView(View):

    @staticmethod
    def get(request):
        if request.user.is_authenticated():
            django_logout(request)
        return redirect('photos_home')
