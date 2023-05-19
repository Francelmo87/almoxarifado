from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .form import ProdutoForm
from .models import Produto


# Create your views here.
def produto_list(request):
    template_name = 'produto_list.html'
    objects = Produto.objects.all()
    context = {'object_list': objects}
    return render(request, template_name, context)


def produto_detail(request, pk):
    template_name = 'produto_detail.html'
    obj = Produto.objects.get(pk=pk)
    context = {'object': obj}
    return render(request, template_name, context)


def produto_add(request):
    form = ProdutoForm(request.POST or None)
    template_name = 'produto_form.html'
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('produto:produto_list'))
    context = {'form': form}
    return render(request, template_name, context)

# def eta_um_add(request):
#     form = EtaUmForm(request.POST or None)
#     template_name = 'eta_um_add.html'
#     if request.method == 'POST':
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect(reverse('eta_um:eta_um_list'))
#     context = {'form': form}
#     return render(request, template_name, context)

#
# def eta_um_update(request, pk):
#     template_name = 'eta_um_update.html'
#     obj = EtaUm.objects.get(pk=pk)
#     form = EtaUmForm(request.POST or None, instance=obj)
#     if request.method == 'POST':
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect(reverse('eta_um:eta_um_list'))
#     context = {'form': form}
#     return render(request, template_name, context)
#
#
# def eta_um_delete(request, pk):
#     obj = EtaUm.objects.get(pk=pk)
#     obj.delete()
#     return HttpResponseRedirect(reverse('eta_um:eta_um_list'))
