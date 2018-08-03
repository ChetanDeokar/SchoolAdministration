from django.conf.urls import url
from views import show_student_dashboard

urlpatterns = [
    url(r'^dashboard/(?P<id>\d+)', show_student_dashboard, name='student_dashboard')
]