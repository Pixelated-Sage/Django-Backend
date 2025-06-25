# Django Restaurant Project

This repository contains the code for a full-featured, Django-based web application simulating a restaurant management system. It was developed as a hands-on project during my comprehensive learning journey through the [Complete Django Developer Course on Udemy](https://www.udemy.com/share/10cI0l3@Rdx-CHLmT5UYec43htQkefxe13nYrqvL09BSEkpITRVn-s9dzDDsAMIdcP_ty9__4w==/).

---

## 🚀 Project Overview & Features

This project serves as a robust demonstration of core Django functionalities, providing a complete backend for a restaurant. Key features and functionalities include:

* **Secure User Authentication:** Implements a complete user management system, allowing for secure registration, login, and logout.
* **Dynamic Product Catalog:** Displays a comprehensive listing of meals (products) with detailed information, images, and accurate stock management.
* **Seamless Order Management:** Enables users to place orders, view their complete order history, and track order status.
* **Intuitive Admin Interface:** Leverages Django's powerful built-in admin panel for efficient management of users, products, orders, and other data models.
* **Custom Template Tags & Filters:** Demonstrates the creation and use of custom Django template tags and filters for extending template capabilities and logic.
* **Robust Static & Media File Handling:** Properly configured to serve static assets (CSS, JavaScript, images) and user-uploaded media files (e.g., meal images).
* **Shopping Cart Functionality:** A foundational implementation for adding items to a cart before checkout (though full checkout integration might be extended in future iterations).

---

## 🛠️ Technologies & Tools Used

The project is built upon a modern and efficient stack:

* **Backend Framework:** **Django 5.x** (Python's high-level web framework)
* **Database:** **MySQL** (configured for production-grade data management, easily swappable to SQLite for development)
* **Frontend Styling:** **Bootstrap 5** (integrated via `django-crispy-forms` for responsive and elegant UI components)
* **Programming Language:** **Python 3.13**
* **Note-Taking & Documentation:** **Obsidian** (used for structuring and organizing personal course notes, available in the `/notes` folder)

---

## 📂 Project Structure

The repository follows a standard Django project layout, promoting modularity and maintainability:

```

├── manage.py
├── mysite/                 \# Main Django project configuration
│   ├── settings.py         \# Project settings (database, apps, etc.)
│   ├── urls.py             \# Project-level URL routing
│   └── wsgi.py             \# WSGI configuration for deployment
│   └── asgi.py             \# ASGI configuration (for async, if used)
├── restaurant/             \# Core application for restaurant features
│   ├── models.py           \# Database schema definitions
│   ├── views.py            \# Business logic and request handling
│   ├── urls.py             \# App-specific URL routing
│   ├── templates/          \# HTML templates for rendering pages
│   ├── static/             \# App-specific static files (CSS, JS, images)
│   └── admin.py            \# Admin interface configurations
├── media/                  \# Directory for user-uploaded files
│   └── meal\_images/        \# Example: uploaded meal photos
├── notes/                  \# Personal learning notes from the course
│   └── \*.md                \# Markdown files created with Obsidian
├── .venv/                  \# Python virtual environment (ignored by Git)
├── requirements.txt        \# List of Python dependencies
└── README.md               \# Project documentation

````

---

## 📝 How to Run Locally

Follow these steps to set up and run the Django Restaurant Project on your local machine:

1.  **Clone the Repository:**
    Start by cloning the project to your local system:
    ```bash
    git clone [https://github.com/Pixelated-Sage/Django-Backend.git](https://github.com/Pixelated-Sage/Django-Backend.git)
    cd Django-Backend
    ```

2.  **Create and Activate a Virtual Environment:**
    It's best practice to use a virtual environment to manage project dependencies:
    ```bash
    python3 -m venv .venv
    source .venv/bin/activate  # On Windows, use `.\.venv\Scripts\activate`
    ```

3.  **Install Dependencies:**
    Install all required Python packages listed in `requirements.txt`:
    ```bash
    pip install -r requirements.txt
    ```

4.  **Configure Your Database:**
    The project is set up to use MySQL by default.
    * **For MySQL:** Ensure you have MySQL running and update the `DATABASES` configuration in `mysite/settings.py` with your credentials.
    * **For SQLite (Quick Setup):** For rapid testing, you can uncomment or adjust the `DATABASES` setting in `mysite/settings.py` to use SQLite (Django's default) by ensuring it looks something like this:
        ```python
        DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.sqlite3',
                'NAME': BASE_DIR / 'db.sqlite3',
            }
        }
        ```

5.  **Apply Migrations:**
    Run database migrations to create the necessary tables:
    ```bash
    python manage.py migrate
    ```

6.  **Create a Superuser:**
    Create an administrative user to access the Django admin panel:
    ```bash
    python manage.py createsuperuser
    ```
    Follow the prompts to set a username, email, and password.

7.  **Run the Development Server:**
    Start the Django development server:
    ```bash
    python manage.py runserver
    ```

8.  **Access the Application:**
    Open your web browser and navigate to: [http://localhost:8000/](http://localhost:8000/)
    You can access the admin panel at [http://localhost:8000/admin/](http://localhost:8000/admin/) using the superuser credentials you created.

---

## 📚 My Learning Journey & Course Experience

This project is a direct outcome of diligently following the **[Complete Django Developer Course on Udemy](https://www.udemy.com/share/10cI0l3@Rdx-CHLmT5UYec43htQkefxe13nYrqvL09BSEkpITRVn-s9dzDDsAMIdcP_ty9__4w==/)**. The course provided an incredibly comprehensive and hands-on approach to mastering Django development.

Throughout the course, I gained in-depth knowledge and practical experience in:

* **Model-View-Controller (MVC) / Model-View-Template (MVT) Architecture:** Understanding Django's core design patterns.
* **Database Interactions (ORM):** Utilizing Django's powerful Object-Relational Mapper to interact with databases without writing raw SQL.
* **URL Routing & Views:** Defining clean and efficient URL patterns and writing logic to handle web requests.
* **Template Engine:** Rendering dynamic HTML content using Django's template language.
* **Forms & Validation:** Creating and processing web forms securely and effectively.
* **User Authentication & Authorization:** Implementing robust security features for user management.
* **Django Admin Customization:** Extending and leveraging the built-in admin interface for specific project needs.
* **Static and Media File Management:** Correctly serving CSS, JavaScript, images, and user-uploaded content.
* **Deployment Best Practices:** Insights into preparing Django applications for production environments.

My personal notes, summaries, and code snippets from the course, meticulously organized with **Obsidian**, are available in the `/notes` directory. These notes reflect my active learning process and can serve as a quick reference for key Django concepts.

---

## 🏆 Course Certificate

I am proud to have successfully completed the course and earned my certificate of completion:

* **[View My Certificate on Udemy](https://www.udemy.com/certificate/UC-70b96f64-2c4e-4f19-b81a-6b4f8ea357d8/)**

---

## 🤝 Contributing & Feedback

Contributions, suggestions, and feedback are highly welcome! If you have ideas for improvements, new features, or find any issues, please feel free to:

* Open an issue to discuss your proposed changes.
* Submit a pull request with your enhancements.

---

## 📄 License

This project is intended for educational purposes and as a portfolio piece showcasing my Django development skills.

---

**Thank you for exploring my Django Restaurant Project!**
````
