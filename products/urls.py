from django.urls import path

from products.views import *

urlpatterns = [
    path('', home, name="home"),
    path('pottery-classes/', pottery_classes, name="pottery"),
    path('pottery-class/<int:id>/', pottery_class, name="pottery_class"),

    path('artists/', artists, name="artists"),
    path('artist-bio/<int:id>/', artist_bio, name="artist_bio"),

    path('login/', LoginView.as_view(), name="login"),
    path('login/register/', RegisterPage.as_view(), name="register"),
    path('account/', account, name="account"),

    path('order/<int:id>/', order, name="order"),

    path('about-us/', about_us, name="about_us"),
]
