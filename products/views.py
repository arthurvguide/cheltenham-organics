"""
products/views.py: views to display all pages in the products app.
It was inspired by Code Institute's Boutique Ado project,
but adapted for my project. Delete_reviw views was necessary to handle
my "original models".
"""

from django.shortcuts import render, redirect, reverse, get_object_or_404, HttpResponse
from django.contrib import messages
from django.db.models import Q
from django.contrib.auth.decorators import login_required

from .models import Product, Category, Review
from .forms import ReviewForm

from profiles.models import WishList, UserProfile


def get_products(request):
    """ A view to show all products, including sorting and search queries """

    products = Product.objects.all()
    query = None
    categories = None

    if request.GET:

        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "No searchs has been inputed")
                return redirect(reverse('products'))

            queries = Q(name__icontains=query)
            products = products.filter(queries)

    context = {
        'products': products,
        'search_term': query,
        'query_category': categories,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """ A view to show individual product details """

    product = get_object_or_404(Product, pk=product_id)
    reviews = Review.objects.filter(product=product)

    if request.user.is_authenticated:
        current_user = UserProfile.objects.filter(user=request.user).first()
        wishlist = WishList.objects.filter(product=product, user=current_user)

        if request.method == 'POST':

            review_form = ReviewForm(data=request.POST or None)

            if request.user.is_authenticated and review_form.is_valid():

                review = review_form.save(commit=False)
                review.product = product
                review.user = current_user.user
                review.save()
                product.save()

                context = {
                   'product': product,
                   'reviews': reviews,
                   'wishlist': wishlist,
                   'review_form': ReviewForm(),
                  }
                return render(request, 'products/product_detail.html', context)

            else:
                context = {
                   'product': product,
                   'reviews': reviews,
                   'wishlist': wishlist,
                   'review_form': ReviewForm(),
                  }
                return render(request, 'products/product_detail.html', context)

        else:
            context = {
                'product': product,
                'reviews': reviews,
                'wishlist': wishlist,
                'review_form': ReviewForm(),
                }
            return render(request, 'products/product_detail.html', context)

    else:
        context = {
                   'product': product,
                   'reviews': reviews,
                  }

        return render(request, 'products/product_detail.html', context)


@login_required
def delete_review(request, review_id):
    """
    Removes the review from the product
    """

    review = get_object_or_404(Review, pk=review_id)
    product = review.product

    try:
        review.delete()

    except Exception as e:
        messages.error(request, f'Error removing review: {e}')
        return HttpResponse(status=500)

    return redirect(reverse('product_detail', args=[product.id]))
