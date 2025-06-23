from django.urls import path
from .views import index , order , details , login , logout_user


urlpatterns = [
    path('', index, name="index"),
    path('order/<int:pk>/', order, name='order'),
    path('details/', details, name='details'),
    path('/login/', login, name='login'),
    path('/logout/', logout_user, name='logout'),

]