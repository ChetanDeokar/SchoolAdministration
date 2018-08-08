# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth import authenticate
from django.shortcuts import render, redirect

from forms import LoginForm
# Create your views here.

def show_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(request, username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            if user is not None:
                usertype = user.usertype
                if usertype == 'TE':
                    return redirect('teacher_dashboard', id=user.id)
                elif usertype == 'ST':
                    return redirect('student_dashboard', id=user.id)
                elif usertype == 'HM':
                    return redirect('hm_dashboard', id=user.id)
            else:
                form.add_error(None, "Authentication Failed")
                return render(request, 'login.html', {'form': form})
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})
