from django.conf.urls import url, include
from views import show_login

urlpatterns = [
    url(r'^$', show_login, name='login'),
    url(r'^validate/$', show_login, name='validate_user'),
]