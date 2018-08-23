# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import UserPassesTestMixin
from django.http import HttpResponse
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views import View

# Create your views here.


class StudentView(UserPassesTestMixin, View):

    @method_decorator(login_required)
    def get(self, request, id):
        UserModel = get_user_model()
        user_obj = UserModel.objects.get(id=id)
        if user_obj.id == request.user.id:
            return render(request, 'student.html', {'id': id})
        else:
            return HttpResponse('Unauthorized', status=401)

    def test_func(self):
        return self.request.user.groups.filter(name='student').exists()
