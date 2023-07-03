from django.urls import path

from products.views import *

urlpatterns = [
    path('', home),
    path('pottery-classes/', pottery_classes, name="pottery"),
    path('pottery-class/<int:id>/', pottery_class, name="pottery_class"),
    path('artists/', artists, name="artists"),
    path('artist-bio/<int:id>/', artist_bio, name="artist_bio"),
    path('account/', account, name="account"),
    path('account/register/', register, name="register"),
    path('cart/', cart, name="cart"),

]
