from django.urls import path
from almox.produto import views as v

app_name = 'produto'


urlpatterns = [
    path('', v.produto_list, name='produto_list'),
    path('<int:pk>', v.produto_detail, name='produto_detail'),
    path('add/', v.produto_add, name='produto_add'),
    path('edit/<int:pk>', v.produto_update, name='produto_update'),
    path('delete/<int:pk>', v.produto_delete, name='produto_delete'),
]
