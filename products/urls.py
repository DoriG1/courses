from django.urls import path
from django.contrib.auth.views import LogoutView

from products.views import *

urlpatterns = [
    path('', home, name="home"),
    path('pottery-classes/', pottery_classes, name="pottery"),
    path('pottery-class/<slug:slug>/', pottery_class, name="pottery_class"),

    path('artists/', artists, name="artists"),
    path('artist-bio/<slug:slug>/', artist_bio, name="artist_bio"),

    path('login/', LoginView.as_view(), name="login"),
    path('login/register/', RegisterPage.as_view(), name="register"),
    path('logout/', LogoutView.as_view(next_page='home'), name='logout'),

    path('account/', account, name="account"),

    path('order/<slug:slug>/', order, name="order"),

    path('about-us/', about_us, name="about_us"),
]
