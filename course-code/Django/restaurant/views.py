from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth import authenticate, login as auth_login, logout
from restaurant.models import Meal,OrderTransaction
from django.shortcuts import render , redirect
from django.http import HttpResponse
from .form import UserLoginForm
from django.views import View
from http import HTTPStatus

def error_404_view(request, exception):
    return render(request, 'index', status=404)


class IndexView(View):
    def get(self, request):
        # Only get meals with stock > 0
        meals = Meal.objects.filter(stock__gt=0)
        context = {
            'meals': meals,
        }
        return render(request=request, template_name="restaurant/index.html", context=context)


class OrderView(ListView):
    context_object_name = 'transaction'
    template_name = 'restaurant/details.html'

    def get_queryset(self):
        return OrderTransaction.objects.filter(customer=self.request.user)



class DetailsView(View):
    def get(self, request):
        transaction = OrderTransaction.objects.filter(customer=request.user)

        context = {
            'transaction': transaction,
        }

        return render(request=request, template_name="restaurant/details.html", context=context)
    

class CustomLoginView(View):
    form_class = UserLoginForm
    template_name = "restaurant/login.html"

    def get(self, request):
        login_form = self.form_class()
        login_form.fields['username'].widget.attrs['placeholder'] = 'Your Username'
        login_form.fields['password'].widget.attrs['placeholder'] = 'Your Password'
        context = {
        'login_form': login_form,
        }
        return render(request=request, template_name=self.template_name, context=context)
    
    def post(self, request):
        login_form = self.form_class(data = request.POST)
        if login_form.is_valid():
            username = login_form.cleaned_data.get('username')
            password = login_form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth_login(request, user)
                return redirect("details")
            login_form.add_error(None, "Invalid username or password")
        context = {
        'login_form': login_form,
        }
        return render(request=request, template_name=self.template_name, context=context)

def logout_user(request):
    logout(request)
    return redirect("index")