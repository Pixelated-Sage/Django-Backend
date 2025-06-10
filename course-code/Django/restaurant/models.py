from django.db import models

# Create your models here.
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

    #Stock of the meal
    stock = models.IntegerField("Stock of Meal", default=0)

    def __str__(self):
        return self.description if self.description else self.name