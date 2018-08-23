from django.conf.urls import url
from views import StudentView

urlpatterns = [
    url(r'^dashboard/(?P<id>\d+)', StudentView.as_view(), name='student_dashboard')
]