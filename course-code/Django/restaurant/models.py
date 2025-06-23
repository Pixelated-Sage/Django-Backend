from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now
# Create your models here.

DELIVERY_STATUS_CHOICES = (
    ('PENDING', 'Pending'),
    ('IN_PROGRESS', 'In Progress'),
    ('DELIVERED', 'Delivered'),
    ('CANCELLED', 'Cancelled'),
)

class Meal(models.Model):
    #Name of the meal
    name = models.CharField("Name of Meal", max_length=100)

    #Description of the meal
    #Optional Field.
    description = models.TextField("Description of Meal" , max_length=500 , blank=True , null=True)

    #Price of the meal 
    price = models.DecimalField("Price of Meal", max_digits=10, decimal_places=2)

    #Availability of the meal (boolean true or false)
    available = models.BooleanField("Is Meal Available?", default=True)

    image = models.ImageField("Image of Meal", upload_to='meal_images', default='meal_images/default_meal.jpg', blank=True, null=True)

    #Stock of the meal
    stock = models.IntegerField("Stock of Meal", default=0)

    def __str__(self):
        return self.description if self.description else self.name
    
class OrderTransaction(models.Model):
    meal = models.ForeignKey(Meal, on_delete=models.CASCADE)

    customer = models.ForeignKey(User, on_delete=models.CASCADE)

    amount = models.DecimalField("Amount of Meal Ordered", default=64, decimal_places=2, max_digits=10)

    status = models.CharField("Status of Delivery", max_length=20, choices=DELIVERY_STATUS_CHOICES, default='PENDING')

    created_at = models.DateTimeField("Order Created At" , default=now)

