from http import HTTPStatus
from django.shortcuts import render
from django.http import HttpResponse
from restaurant.models import Meal
# Create your views here.

def index(request):
    if request.method == "GET":

        return render(request=request, template_name="restaurant/index.html", context={
            "meals": Meal.objects.all()})
    return HttpResponse(HTTPStatus.BAD_REQUEST)