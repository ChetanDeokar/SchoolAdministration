from django.conf.urls import url
from views import TeacherView

urlpatterns = [
    url(r'dashboard/(?P<id>\d+)/$', TeacherView.as_view(), name='teacher_dashboard'),
]