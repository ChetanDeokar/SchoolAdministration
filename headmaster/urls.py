from django.conf.urls import url
from views import HeadMasterDashboardView

urlpatterns = [
    url(r'^dashboard/(?P<id>\d+)', HeadMasterDashboardView.as_view(), name='hm_dashboard')
]