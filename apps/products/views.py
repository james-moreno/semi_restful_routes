from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.contrib import messages
from .models import Product
#from django.core.urlresolvers import reverse
# Create your views here.


def products(request):
    context = {"products": Product.objects.all()}
    return render(request, 'products/products.html', context)


def new_product(request):
    return render(request, 'products/new_product.html')


def create_new_product(request):
    if request.method == "POST":
        product_data = Product.objects.create_new_product(request.POST)
        if product_data['created']:
            messages.success(request, "Successfully added {}.".format(product_data['new_product'].name))
        else:
            for error in product_data['errors']:
                messages.error(request, error)
        return redirect(reverse('products:new_product'))


def show(request, id):
    context = {"product": Product.objects.get(id=id)}
    return render(request, 'products/show_product.html', context)


def update(request, id):
    if request.method == "POST":
        product_data = Product.objects.update_product(id, request.POST)
        if product_data['updated']:
            messages.success(request, "Succesfully updated {}.".format(product_data['updated_product'].name))
        else:
            for error in product_data['errors']:
                messages.error(request, error)
        return redirect(reverse('products:edit', kwargs={'id': id}))


def edit(request, id):
    context = {"product": Product.objects.get(id=id)}
    return render(request, 'products/edit.html', context)


def destroy(request, id):
    Product.objects.filter(id=id).delete()
    return redirect('/products')
