from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url('register', views.register, name='register'),
    url('Login', views.Login, name='Login'),
    url('analysis', views.analysis, name='analysis'),
    url('api', views.api, name='api'),
    url('submit', views.submit, name='submit'),
]