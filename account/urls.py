from django.conf.urls import url
from django.urls import path

from account import views
from django.contrib.auth import views as auth_views

app_name = 'account'
urlpatterns = [
    # url(r'^login/$', views.user_login, name='login'),
    url(r'^login/$', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
