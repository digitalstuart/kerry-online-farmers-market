from django.shortcuts import render, redirect, reverse
from .models import Seller
from .forms import SellerForm

def all_sellers(request):
    sellers = Seller.objects.all()
    return render(request, "sellers.html", {"sellers": sellers})

def add_seller(request):
    if request.method == "POST":
        form = SellerForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            sellers = Seller.objects.all()
            return redirect(reverse("sellers"))
    else:
        form = SellerForm
    return render(request, "sellers_form.html", {"form": form})