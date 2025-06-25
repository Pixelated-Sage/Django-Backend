## Why use Django

- DRF Principle
- Full Stack Nature
- Object Relationship Mapping (ORM)

## Overview of Features and Capabilities

- MVT architecture
	- Django follows the model-view-template (MVT) architectural pattern.
	- Model - Represents the data structure. it interacts with the database.
	- View Handles the logic of your application and controls what data is displayed in the template
	- Template - render the HTML 
	- ORM - interact with database
	- Admin panel
	- form handling - validation user input
	- authentication and authorization
- Scalability
- Template Engine


## Django Setup Commands


- `python3 -m venv .venv
- `source .venv/bin/activate
- `python -m django help
-  `django-admin startproject mysite ./Django
- `python manage.py startapp restaurant
-  `python manage.py migrate
-  `python manage.py runserver localhost:9000


## Files Structure

![Pasted image 20250608120256](img/Pasted%20image%2020250608120256.png)



- `manage.py` - to do the administrative task for the application
- `db.sqlite3` - the database of the web page
- `settings.py` - configs entire Django project 
- `url.py` - all URL routes
- `wsgi` - entry point
- `asgi.py` - entry point for asynchronous  
- `__init__.py` - for scaling the project modules
- `models.py` - Data structure of the application
- `views.py` - rendering and responding or templates
- `tests.py` - unit test for components
- `admin.py` - the admin interface
- `apps.py` - app config class 
- `migration.py` - blueprint of all changes in database


