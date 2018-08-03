from django.conf.urls import url
from views import show_teacher_dashboard

urlpatterns = [
    url(r'dashboard/(?P<id>\d+)/$', show_teacher_dashboard,name='teacher_dashboard'),
]