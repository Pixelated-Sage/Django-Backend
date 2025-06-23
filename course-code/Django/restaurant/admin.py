from django.contrib import admin
from .models import Meal
from .models import OrderTransaction

@admin.register(Meal)
class MealAdmin(admin.ModelAdmin):
    list_display = ('name','description','price','available', 'image', 'stock')

    search_fields = ('name', 'description','price')

@admin.register(OrderTransaction)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('meal', 'customer', 'amount', 'status', 'created_at')
    search_fields = ('meal__name', 'customer__username', 'status')
    
# Register your models here.
# admin.site.register(Meal, MealAdmin)