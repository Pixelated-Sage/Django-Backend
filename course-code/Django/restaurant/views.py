from http import HTTPStatus
from django.shortcuts import render , redirect
from django.http import HttpResponse
from restaurant.models import Meal,OrderTransaction
from .form import UserLoginForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login as auth_login, logout
# Create your views here.

def index(request):
    if request.method == "GET":
        meals = []

        temp_list = []

        all_meals = Meal.objects.all()
        
        for cnt in range(all_meals.count()):
            if cnt % 3 == 0 and cnt != 0:
                meals.append(temp_list)
                temp_list = []
            temp_list.append(all_meals[cnt])
        context = {
            'meals':meals,
        }
        return render(request=request, template_name="restaurant/index.html", context={
            "meals": Meal.objects.all()})
    return HttpResponse(HTTPStatus.BAD_REQUEST)

def order(request , pk = None):
    if pk:
        got_meal = Meal.objects.filter(id = pk).last()

        if got_meal and got_meal.stock > 0:
            OrderTransaction.objects.create(meal = got_meal, customer = request.user, amount = got_meal.price)
            got_meal.stock -= 1

            got_meal.save()

            return redirect("index")
    return HttpResponse(HTTPStatus.BAD_REQUEST)

@login_required
def details(request):
    transaction = OrderTransaction.objects.filter(customer=request.user)

    context = {
        'transaction': transaction,
    }

    return render(request=request, template_name="restaurant/details.html", context=context)


def login(request):
    login_form = UserLoginForm(request.POST or None)
    if request.method == "POST":
        if login_form.is_valid():
            username = login_form.cleaned_data.get('username')
            password = login_form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth_login(request, user)
                return redirect("details")
            login_form.add_error(None, "Invalid username or password")

    else:
        login_form = UserLoginForm()
        login_form.fields['username'].widget.attrs['placeholder'] = 'Your Username'
        login_form.fields['password'].widget.attrs['placeholder'] = 'Your Password'
    context = {
        'login_form': login_form,
    }
    return render(request=request, template_name="restaurant/login.html", context=context)

def logout_user(request):
    logout(request)
    return redirect("index")