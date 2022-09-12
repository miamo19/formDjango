from django.shortcuts import render, get_object_or_404, redirect
from .models import Product
from .form import ProductForm


# Create your views here.
def product_create_view(request):
    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = ProductForm()
    context = {
        'form':form
    }
    return render(request, "Blog2/product_create.html", context)

def product_update_view(request, id):
    obj = get_object_or_404(Product, id=id)
    forms = ProductForm(request.POST or None)
    if forms.is_valid():
        forms.save()
        forms = ProductForm()
    context = {
        'form':forms
    }
    return render(request, 'Blog2/product_update.html', context)

def product_list_view(request):
    queryset = Product.objects.all()  #list of object
    context = {
        'object_list': queryset
    }
    return render(request, 'Blog2/product_detail.html', context)

def product_delete_view(request, id):
    obj = get_object_or_404(Product, id=id)
    if request.method == 'POST':
        obj.delete()
        return redirect('list')
    context = {
        'object_list':obj
    }
    return render(request, 'Blog2/product_delete.html', context)
