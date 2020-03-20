from django.shortcuts import render
from .models import Product
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

def all_products(request):
    products = Product.objects.all()
    return render(request, "products.html", {"products": products})

class ProductCreate(CreateView):
    model = Product
    fields = ['name']

class ProductUpdate(UpdateView):
    model = Product
    fields = ['name']

class ProductDelete(DeleteView):
    model = Product
    success_url = reverse_lazy('product-list')



# From the blog project - Creating and editing
def create_or_edit_post(request, pk=None):
    """
    Create a view that allows us to create
    or edit a post depending if the Post ID
    is null or not
    """
    # this line is used to check if there is a product (for editing purposes)
    post = get_object_or_404(Post, pk=pk) if pk else None
    # this is for post (ignore for now)
    if request.method == "POST":
        form = BlogPostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save()
            return redirect(post_detail, post.pk)
    # this is the get.  the instance=post is only important if we found a post earlier (for editing)
    else:
        form = BlogPostForm(instance=post)
    return render(request, 'blogpostform.html', {'form': form})


# just for creating
def create_post(request):
                                            """
                                            Create a view that allows us to create
                                            or edit a post depending if the Post ID
                                            is null or not
                                            """
                                    # this line can get removed as we only care about creating
                                    # post = get_object_or_404(Post, pk=pk) if pk else None
                                    # this is for post (ignore for now)
                                    # if request.method == "POST":
                                    #     form = BlogPostForm(request.POST, request.FILES, instance=post)
                                    #     if form.is_valid():
                                    #         post = form.save()
                                    #         return redirect(post_detail, post.pk)
                                    # # this is the get.  the instance=post is only important if we found a post earlier (for editing)
                                    # else:

#   THis is for just getting a form an putting it on the page.
    form = BlogPostForm()
    return render(request, 'blogpostform.html', {'form': form})