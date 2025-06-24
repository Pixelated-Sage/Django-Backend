from django.test import TestCase , client
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Meal
from .form import UserLoginForm
from django.contrib.auth import get_user
# Create your tests here.

class MealModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Meal.objects.create(name="Test Meal",
                            description="This is a test meal description.", 
                            price=20.23,
                            available=True, 
                            stock=5,
                            )
        
    def test_meal_name(self):
        meal = Meal.objects.get(id=1)
        self.assertEqual(meal.name, "Test Meal")
    
    def test_stock_count(self):
        meal = Meal.objects.get(id=1)
        self.assertEqual(meal.stock, 5)

class ViewsTest(TestCase):
    def test_index_view(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
    
    def test_details_view(self):
        user = User.objects.create(username = "abhi")
        user.set_password('abhi5900')

        user.save()

        response = self.client.login(username='abhi', password='abhi5900')
        self.assertTrue(response)
    def test_details_view_fails(self):
        user = User.objects.create(username = "abhi")
        user.set_password('abhi5900')

        user.save()

        response = self.client.login(username='abhi', password='abhi5900')
        self.assertFalse(response)

class FormsTest(TestCase):
    def test_login_from_user_name_is_required(self):
        form = UserLoginForm()
        self.assertTrue(form.fields['username'].required)
    
    def test_valid_login_form(self):
        User.objects.create_user(username='testuser', password='testpass')
        form = UserLoginForm(data={'username': 'testuser', 'password': 'testpass'})
        self.assertTrue(form.is_valid())

class ClientTest(TestCase):
    def test_login(self):
        user = User.objects.create(username = "testuser")
        user.set_password('testpass')
        user.save()

        c = client.Client()
        c.post('/login/', {'username': 'testuser', 'password': 'testpass'})

        respionse = c.get(reverse('details'))
        self.assertEqual(respionse.status_code, 200)