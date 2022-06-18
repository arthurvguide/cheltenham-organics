from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.contrib import messages

from .models import UserProfile, WishList
from .forms import UserProfileForm

from checkout.models import Order
from products.models import Product

def profile(request):
    """ Display the user's profile. """
    profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully')

    form = UserProfileForm(instance=profile)
    orders = profile.orders.all()

    template = 'profiles/profile.html'
    context = {
        'form': form,
        'orders': orders,
        'on_profile_page': True
    }

    return render(request, template, context)


def order_history(request, order_number):
    order = get_object_or_404(Order, order_number=order_number)

    messages.info(request, (
        f'This is a past confirmation for order number {order_number}.'
    ))

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
        'from_profile': True,
    }

    return render(request, template, context)


def add_wishlist(request):
    pid = request.GET['product']
    product = Product.objects.get(pk=pid)
    current_user = UserProfile.objects.filter(user=request.user).first()
    data = {}
    count_wishlist = WishList.objects.filter(product=product, user=current_user).count()
    if count_wishlist > 0:
        data = {
            'bool': False
        }
    else: 
        WishList.objects.create(
            product=product,
            user=current_user,
        )
        data = {
            'bool': True
        }
    return JsonResponse(data)


def remove_wishlist(request):
    pid = request.GET['product']
    product = Product.objects.get(pk=pid)
    current_user = UserProfile.objects.filter(user=request.user).first()
    wishlist = WishList.objects.filter(product=product, user=current_user)

    wishlist.delete()
    data = {}

    data = {
            'bool': True
        }
    return JsonResponse(data)


def wishlist(request):
    current_user = UserProfile.objects.filter(user=request.user).first()
    wishlist = WishList.objects.filter(user=current_user).order_by('-id')
    context = {
        'wishlist': wishlist
    }
    return render(request, 'profiles/wishlist.html', context)