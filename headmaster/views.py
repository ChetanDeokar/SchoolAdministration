# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.


def show_hm_dashboard(request, id):
    return render(request, 'headmaster.html', {'id': id})
