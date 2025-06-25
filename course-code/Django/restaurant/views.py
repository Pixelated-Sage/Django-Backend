from http import HTTPStatus
from django.shortcuts import render , redirect
from django.http import HttpResponse
from restaurant.models import Meal,OrderTransaction
from .form import UserLoginForm

from django.contrib.auth import authenticate, login as auth_login, logout
from django.views import View

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

def error_404_view(request, exception):
    return render(request, 'index', status=404)

# Create your views here.

class IndexView(View):
    def get(self, request):
        # Only get meals with stock > 0
        meals = Meal.objects.filter(stock__gt=0)
        context = {
            'meals': meals,
        }
        return render(request=request, template_name="restaurant/index.html", context=context)
    

# def index(request):
#     if request.method == "GET":
#         meals = []

#         temp_list = []

#         all_meals = Meal.objects.all()
        
#         for cnt in range(all_meals.count()):
#             if cnt % 3 == 0 and cnt != 0:
#                 meals.append(temp_list)
#                 temp_list = []
#             temp_list.append(all_meals[cnt])
#         context = {
#             'meals':meals,
#         }
#         return render(request=request, template_name="restaurant/index.html", context={
#             "meals": Meal.objects.all()})
#     return HttpResponse(HTTPStatus.BAD_REQUEST)


class OrderView(ListView):
    context_object_name = 'transaction'
    template_name = 'restaurant/details.html'

    def get_queryset(self):
        return OrderTransaction.objects.filter(customer=self.request.user)
    


    # def get(self, request, pk=None):
    #     if pk:
    #         got_meal = Meal.objects.filter(id=pk).last()

    #         if got_meal and got_meal.stock > 0:
    #             OrderTransaction.objects.create(meal=got_meal, customer=request.user, amount=got_meal.price)
    #             got_meal.stock -= 1

    #             got_meal.save()

    #             return redirect("index")
    #     return HttpResponse(HTTPStatus.BAD_REQUEST)
    


# def order(request , pk = None):
#     if pk:
#         got_meal = Meal.objects.filter(id = pk).last()

#         if got_meal and got_meal.stock > 0:
#             OrderTransaction.objects.create(meal = got_meal, customer = request.user, amount = got_meal.price)
#             got_meal.stock -= 1

#             got_meal.save()

#             return redirect("index")
#     return HttpResponse(HTTPStatus.BAD_REQUEST)



class DetailsView(View):
    def get(self, request):
        transaction = OrderTransaction.objects.filter(customer=request.user)

        context = {
            'transaction': transaction,
        }

        return render(request=request, template_name="restaurant/details.html", context=context)
    

# @login_required
# def details(request):
#     transaction = OrderTransaction.objects.filter(customer=request.user)

#     context = {
#         'transaction': transaction,
#     }

#     return render(request=request, template_name="restaurant/details.html", context=context)

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


# def login(request):
#     login_form = UserLoginForm(request.POST or None)
#     if request.method == "POST":
#         if login_form.is_valid():
#             username = login_form.cleaned_data.get('username')
#             password = login_form.cleaned_data.get('password')
#             user = authenticate(request, username=username, password=password)
#             if user is not None:
#                 auth_login(request, user)
#                 return redirect("details")
#             login_form.add_error(None, "Invalid username or password")

#     else:
#         login_form = UserLoginForm()
#         login_form.fields['username'].widget.attrs['placeholder'] = 'Your Username'
#         login_form.fields['password'].widget.attrs['placeholder'] = 'Your Password'
#     context = {
#         'login_form': login_form,
#     }
#     return render(request=request, template_name="restaurant/login.html", context=context)

def logout_user(request):
    logout(request)
    return redirect("index")