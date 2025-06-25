
To achieve the **professional folder structure** you mentioned (with `config/`, `settings/`, `apps/`, etc.), you'll need to **customize your Django project layout** after creating it. Here's a **step-by-step guide** to turn a regular Django project into this structure.

---

## ✅ Step-by-Step to Set Up Custom Django Project Structure

---

### 🧱 **Step 1: Create Your Project**

```bash
django-admin startproject config .
```

Your initial files:

```
manage.py
config/
    ├── __init__.py
    ├── settings.py
    ├── urls.py
    ├── wsgi.py
```

---

### 🧰 **Step 2: Create `settings/` Directory Inside `config/`**

Now move `settings.py` into a new folder:

```bash
mkdir config/settings
mv config/settings.py config/settings/base.py
touch config/settings/__init__.py
```

Then, create separate files:

```bash
touch config/settings/dev.py
touch config/settings/prod.py
```

---

### ⚙️ **Step 3: Split Settings**

#### `config/settings/__init__.py`:

```python
# Load default base settings
from .base import *
```

#### `config/settings/dev.py`:

```python
from .base import *

DEBUG = True
ALLOWED_HOSTS = ['*']
```

#### `config/settings/prod.py`:

```python
from .base import *

DEBUG = False
ALLOWED_HOSTS = ['yourdomain.com']
```

---

### 🔄 **Step 4: Update `manage.py` and `wsgi.py`**

Change `DJANGO_SETTINGS_MODULE` from:

```python
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
```

to:

```python
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings.dev')  # or prod
```

Make this change in both:

- `manage.py`
    
- `config/wsgi.py`
    
- (and `config/asgi.py` if using ASGI)
    

---

### 🏗️ **Step 5: Create `apps/` Directory for Your Django Apps**

```bash
mkdir apps
```

Move your apps here:

```bash
mv contact/ apps/
mv restaurant/ apps/
```

Update `INSTALLED_APPS` in `base.py` accordingly:

```python
INSTALLED_APPS = [
    'apps.contact',
    'apps.restaurant',
    # ...
]
```

---

### 📁 **Step 6: Add Static and Media Folders**

From project root:

```bash
mkdir static
mkdir media
```

Add in `base.py`:

```python
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
```

---

### 📄 **Step 7: Create `.env` and Load It in Settings**

```bash
touch .env
```

Install `python-decouple`:

```bash
pip install python-decouple
```

Update `base.py`:

```python
from decouple import config

SECRET_KEY = config('SECRET_KEY')
DEBUG = config('DEBUG', default=True, cast=bool)
ALLOWED_HOSTS = config('ALLOWED_HOSTS', cast=Csv, default='127.0.0.1,localhost')
```

`.env` example:

```
SECRET_KEY=your-secret-key
DEBUG=True
ALLOWED_HOSTS=127.0.0.1,localhost
```

---

### 🧪 Folder Structure Final Output

```
myproject/
│
├── config/
│   ├── __init__.py
│   ├── urls.py
│   ├── wsgi.py
│   ├── settings/
│   │   ├── __init__.py
│   │   ├── base.py
│   │   ├── dev.py
│   │   └── prod.py
│
├── apps/
│   ├── contact/
│   ├── restaurant/
│   └── ...
│
├── static/
├── media/
├── .env
├── manage.py
└── requirements.txt
```

---

## ⚙️ Would You Like Me To:

- Generate this structure as a zip you can download and start from?
    
- Add production `.env.example` and deployment scripts?
    
- Add a Makefile or shell script to automate dev/prod switching?
    

Let me know — I can prepare that all at once for you.