from django.shortcuts import render

def get_products(request):
    """ A view to return the products page """
    
    return render(request, 'products/products.html')
