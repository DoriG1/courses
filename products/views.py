from django.shortcuts import render
from django.shortcuts import redirect
from django.views.generic.edit import FormView
from django.urls import reverse_lazy

from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

from .forms import OrderForm, RegistrationForm

from .models import Course, Artist


def home(request):
    return render(request, 'products/home.html')



def pottery_classes(request):
    courses = Course.objects.all()
    context = {'courses': courses}
    return render(request, 'products/pottery.html', context)



def pottery_class(request, id):
    course = Course.objects.get(id=id)
    context = {'course': course}
    return render(request, 'products/pottery_class.html', context)



def artists(request):
    artists = Artist.objects.all()
    context = {'artists': artists}
    return render(request, 'products/artists.html', context)



def artist_bio(request, id):
    artist = Artist.objects.get(id=id)
    courses = Course.objects.filter(teacher=artist)
    context = {'artist': artist, 'courses': courses}

    return render(request, 'products/artist_bio.html', context)


def cart(request):
    return render(request, 'products/cart.html')


def about_us(request):
    return render(request, 'products/about_us.html')


def checkout(request):
    return render(request, 'products/checkout.html')


def order(request, id):
    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save()
            order.user = request.user
            order.course = Course.objects.get(id=id)
            form.save()
            return render(request, 'products/home.html')
    else:
        form = OrderForm()
        course = Course.objects.get(id=id)

    return render(request, 'products/order.html', {"form": form, 'course': course})



class LoginView(LoginView):
    template_name = 'products/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('home')


class RegisterPage(FormView):
    template_name = 'products/register.html'
    form_class = RegistrationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super().form_valid(form)
    
    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('home')
        return super().get(*args, **kwargs)