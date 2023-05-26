from django.http import HttpResponseRedirect, JsonResponse
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


def produto_add(request):
    form = ProdutoForm(request.POST or None)
    template_name = 'produto_form.html'
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('produto:produto_list'))
    context = {'form': form}
    return render(request, template_name, context)


def produto_update(request, pk):
    template_name = 'produto_update.html'
    obj = Produto.objects.get(pk=pk)
    form = ProdutoForm(request.POST or None, instance=obj)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('produto:produto_list'))
    context = {'form': form}
    return render(request, template_name, context)


def produto_delete(request, pk):
    obj = Produto.objects.get(pk=pk)
    obj.delete()
    return HttpResponseRedirect(reverse('produto:produto_list'))


def produto_detail(request, pk):
    template_name = 'produto_detail.html'
    obj = Produto.objects.get(pk=pk)
    context = {'object': obj}
    return render(request, template_name, context)


def produto_json(request, pk):
    # Retorna o produto, id e estoque.
    produto = Produto.objects.filter(pk=pk)
    data = [item.to_dict_json() for item in produto]
    return JsonResponse({'data': data})
