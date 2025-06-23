
**This helps us to work with SQL database change add and use all the commands of SQL without using any SQL commands 
lets start to do some changes 

`python manage.py shell`
this command opens the shell for the Django

**important command as to call which model to change**
`from restaurant.models import Meal`

- **To add Object or to add entry in SQL**
	`Meal.objects.create(name="Meal 1", description="this is meal 1", price = "20")`
	`Meal.objects.create(name="Meal 2", description="this is meal 2", price = "24")`

![[Pasted image 20250609123109.png]]

- **To Show the Objects**
	`Meal.object.all()`
- **To exit**
	`exit()`

### SQL

![[Pasted image 20250609123253.png]]

**To make changes in the current database**

![[Pasted image 20250609123337.png]]


