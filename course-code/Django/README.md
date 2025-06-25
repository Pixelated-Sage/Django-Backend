# Django Restaurant Project

This repository contains the code for my Django-based restaurant web application, built as part of my learning journey through the [Complete Django Developer Course on Udemy](https://www.udemy.com/share/10cI0l3@Rdx-CHLmT5UYec43htQkefxe13nYrqvL09BSEkpITRVn-s9dzDDsAMIdcP_ty9__4w==/).

## 🚀 Project Overview

- **Live Demo:** _Coming Soon_
- **Course Certificate:** _Available on request_

This project demonstrates a full-featured restaurant backend, including:
- User authentication (login/logout)
- Product (meal) listing with images and stock management
- Order placement and order history
- Admin management via Django admin
- Custom template tags and static/media file handling

## 🛠️ Technologies Used

- **Django 5.x**
- **MySQL** (can be switched to SQLite for quick setup)
- **Bootstrap 5** (via crispy-forms)
- **Python 3.13**
- **Obsidian** for course notes (see `/notes` folder)

## 📂 Project Structure

```
├── manage.py
├── mysite/
│   ├── settings.py
│   ├── urls.py
│   └── ...
├── restaurant/
│   ├── models.py
│   ├── views.py
│   ├── templates/
│   ├── static/
│   └── ...
├── media/
│   └── meal_images/
├── notes/
│   └── *.md   # Obsidian course notes
└── README.md
```

## 📝 How to Run Locally

1. **Clone the repository:**
    ```bash
    git clone https://github.com/Pixelated-Sage/Django-Backend.git
    cd Django-Backend
    ```

2. **Create and activate a virtual environment:**
    ```bash
    python3 -m venv .venv
    source .venv/bin/activate
    ```

3. **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4. **Configure your database:**
    - By default, the project uses MySQL. You can switch to SQLite in `mysite/settings.py` for quick testing.

5. **Apply migrations:**
    ```bash
    python manage.py migrate
    ```

6. **Create a superuser:**
    ```bash
    python manage.py createsuperuser
    ```

7. **Run the development server:**
    ```bash
    python manage.py runserver
    ```

8. **Access the app:**
    - Visit [http://localhost:8000/](http://localhost:8000/) in your browser.

## 📚 Learning Journey

This project was built while following the [Complete Django Developer Course on Udemy](https://www.udemy.com/share/10cI0l3@Rdx-CHLmT5UYec43htQkefxe13nYrqvL09BSEkpITRVn-s9dzDDsAMIdcP_ty9__4w==/).
- All major Django concepts are covered: models, views, templates, forms, authentication, admin, static/media files, and deployment best practices.
- My personal notes and summaries from the course are available in the `/notes` directory as Markdown files (created with Obsidian).

## 🏆 Certificate

I have completed the course and earned a certificate, which is available upon request.

## 🤝 Contributing

Pull requests and suggestions are welcome! For major changes, please open an issue first to discuss what you would like to change.

## 📄 License

This project is for educational purposes.

---

**Thank you for checking out my Django Restaurant Project!**
