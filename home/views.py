from django.shortcuts import render

def get_home(request):
    """ A view to return the home page """
    
    return render(request, 'home/index.html')
