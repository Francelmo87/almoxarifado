from django.urls import path, include
from almox.estoque import views as v

app_name = 'estoque'


entrada_patterns = [
    path('', v.estoque_entrada_list, name='estoque_entrada_list'),
    path('<int:pk>/', v.estoque_entrada_detail, name='estoque_entrada_detail'),
    path('add/', v.estoque_entrada_add, name='estoque_entrada_add'),
]

saida_patterns = [
    path('', v.estoque_saida_list, name='estoque_saida_list'),
    path('<int:pk>/', v.estoque_saida_detail, name='estoque_saida_detail'),
    path('add/', v.estoque_saida_add, name='estoque_saida_add'),
]


urlpatterns = [
    path('entrada/', include(entrada_patterns)),
    path('saida/', include(saida_patterns)),


]
