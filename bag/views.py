from django.shortcuts import render

def get_bag(request):
    """ A view to return the home page """
    
    return render(request, 'bag/bag.html')
