# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.


def show_teacher_dashboard(request, id):
    return render(request, 'teacher.html', {'id': id})
