from django.shortcuts import render

def get_home(request):
    """ A view to return the home page """
    
    return render(request, 'home/index.html')


def privacy_notice(request):
    """ A view to return the privacy_notice """
    
    return render(request, 'home/privacy-notice.html')


def terms_of_use(request):
    """ A view to return the terms of use page """
    
    return render(request, 'home/terms-of-use.html')