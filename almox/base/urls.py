from django.urls import path
from django.contrib.auth.views import LogoutView, LoginView
from almox.base import views as v


app_name = 'base'


urlpatterns = [
    path('', v.index, name='index'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
