from django.conf.urls import url
from views import show_hm_dashboard

urlpatterns = [
    url(r'^dashboard/(?P<id>\d+)', show_hm_dashboard, name='hm_dashboard')
]