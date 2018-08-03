# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.template.loader import get_template

from forms import LoginForm
# Create your views here.


def show_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            usertype = form.cleaned_data['usertype']
            if usertype == 'TE':
                return redirect('teacher_dashboard', id=1)
            elif usertype == 'ST':
                return redirect('student_dashboard', id=2)
            elif usertype == 'HM':
                return redirect('hm_dashboard', id=3)
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})
