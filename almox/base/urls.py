from django.urls import path
from almox.base import views as v


app_name = 'base'


urlpatterns = [
    path('', v.index, name='index'),
]
