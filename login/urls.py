from django.conf.urls import url, include
from views import LoginView, LogoutView

urlpatterns = [
    url(r'^$', LoginView.as_view(), name='login'),
    url(r'^validate/$', LoginView.as_view(), name='validate_user'),
    url(r'^logout/$', LogoutView.as_view(), name='logout'),
]