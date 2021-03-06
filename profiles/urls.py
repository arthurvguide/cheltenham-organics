from django.urls import path
from . import views

urlpatterns = [
    path('', views.profile, name='profile'),
    path('add_wishlist', views.add_wishlist, name='add_wishlist'),
    path('remove_wishlist', views.remove_wishlist, name='remove_wishlist'),
    path('wishlist', views.wishlist, name='wishlist'),
    path('positive_feedback', views.send_positive_feedback, name='positive_feedback'),
    path('negative_feedback', views.send_negative_feedback, name='negative_feedback'),
]