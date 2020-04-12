from django.shortcuts import render


def homepage(request):
    """Renders the homepage"""
    return render(request, "market.html")