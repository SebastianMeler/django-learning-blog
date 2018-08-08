from django.conf.urls import url
from account import views

app_name = 'account'
urlpatterns = [
    url(r'^login/$', views.user_login, name='login')
]
