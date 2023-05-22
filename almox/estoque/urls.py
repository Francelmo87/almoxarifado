from django.urls import path
from almox.estoque import views as v

app_name = 'estoque'

urlpatterns = [
    path('', v.estoque_entrada_list, name='estoque_entrada_list'),
    path('<int:pk>', v.estoque_entrada_detail, name='estoque_entrada_detail'),
    #     path('add/', v.estoque_add, name='estoque_add'),
    #     path('edit/<int:pk>', v.estoque_update, name='estoque_update'),
    #     path('delete/<int:pk>', v.estoque_delete, name='estoque_delete'),
]
