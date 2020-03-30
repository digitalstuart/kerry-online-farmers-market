from django.shortcuts import render
from .models import Seller

def all_sellers(request):
    sellers = Seller.objects.all()
    return render(request, "sellers.html", {"sellers": sellers})