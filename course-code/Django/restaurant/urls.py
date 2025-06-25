from django.urls import path
from .views import IndexView , OrderView , DetailsView , CustomLoginView , logout_user
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', IndexView.as_view(), name="index"),
    path('order/<int:pk>/', login_required(OrderView.as_view()), name='order'),
    path('details/', login_required(DetailsView.as_view()), name='details'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
]