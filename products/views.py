from django.shortcuts import render, redirect, get_object_or_404
from .models import Product
from .forms import ProductForm

def all_products(request):
    products = Product.objects.all()
    return render(request, "products.html", {"products": products})

# From the blog project - Creating and editing
def add_or_edit_product(request, pk=None):
    """
    Create a view that allows us to create
    or edit a post depending if the Post ID
    is null or not
    """
    # this line is used to check if there is a product (for editing purposes)
    products = Product.objects.all()
    product = get_object_or_404(Product, pk=pk) if pk else None
    # this is for post (ignore for now)
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            product = form.save()
            return render(request, "products.html", {"products": products})
    # this is the get.
    # the instance=post is only important if we found a post earlier (for editing)
    else:
        form = ProductForm(instance=product)
    return render(request, 'product_form.html', {'form': form})