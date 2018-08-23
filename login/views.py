# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth import authenticate, login
from django.contrib.auth.models import Group
from django.contrib.auth.views import logout_then_login
from django.shortcuts import render, redirect
from django.views import View

from forms import LoginForm
# Create your views here.


class LoginView(View):

    def get(self, request):
        form = LoginForm()
        return render(request, 'login.html', {'form': form})

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(request, username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    usertype = user.usertype
                    if usertype == 'TE':
                        group = Group.objects.get(name='teacher')
                        user.groups.add(group)
                        return redirect('teacher_dashboard', id=user.id)
                    elif usertype == 'ST':
                        group = Group.objects.get(name='student')
                        user.groups.add(group)
                        return redirect('student_dashboard', id=user.id)
                    elif usertype == 'HM':
                        group = Group.objects.get(name='headmaster')
                        user.groups.add(group)
                        return redirect('hm_dashboard', id=user.id)
            else:
                form.add_error(None, "Authentication Failed.Please Enter Correct Email Id And Password.")
                return render(request, 'login.html', {'form': form})


class LogoutView(View):

    def get(self, request):
        return logout_then_login(request)
