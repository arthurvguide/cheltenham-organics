from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_home, name='home'),
    path('privacy-notice', views.privacy_notice, name='privacy_notice'),
    path('terms_of_use', views.terms_of_use, name='terms_of_use'),
]

