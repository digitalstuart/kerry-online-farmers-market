from django.shortcuts import render, redirect, get_object_or_404, reverse
from .models import Product
from .forms import ProductForm
from django.views.generic import DeleteView
from django.core.urlresolvers import reverse_lazy


def all_products(request):
    products = Product.objects.all()
    return render(request, "products.html", {"products": products})


def add_or_edit_product(request, pk=None):
    """
    View that allows us to create or edit
    a product depending on whether the
    product ID is null or not
    """
    product = get_object_or_404(Product, pk=pk) if pk else None

    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            product = form.save(commit=False)
            product.user = request.user
            product.save()
            products = Product.objects.all()
            return redirect(reverse("products"))
    else:
        form = ProductForm(instance=product)
    return render(request, 'product_form.html', {'form': form})


class delete_product(DeleteView):
    """
    Allows user to delete a product
    Return to products page after deletion
    """
    model = Product
    template_name = 'products/product_delete.html'
    context_object_name = 'product'
    success_url = reverse_lazy('products')