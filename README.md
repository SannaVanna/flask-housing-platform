# Flask-housing-platform
Housing Platform Website (First Flask Project)

This is my first Flask web development project, created to learn the fundamentals of backend web development using Python and Flask.

# Overview

The project is a housing-themed web application that demonstrates core Flask concepts, including routing, form handling, image uploads, database integration, and template rendering.

The application includes a homepage, an about page, a contact form, image upload functionality, and a page for viewing uploaded images.

# Features

- Homepage with navigation links
- Search bar user interface
- About page
- Contact form submission
- Image upload functionality
- Success message after upload
- View uploaded images
- Database integration
- Flask routing and template rendering

# Technologies Used

- Python
- Flask
- HTML5
- CSS3
- SQLite
- Jinja2

# Project Structure

project/
│
├── app.py
├── requirements.txt
├── Procfile
├── .gitignore
│
├── static/
│   ├── css/
│   └── uploads/
│
├── templates/
│   ├── index.html
│   ├── about.html
│   ├── contact.html
│   ├── success.html
│   └── view_image.html
│
└── database.db

Deployment Files

requirements.txt

Contains the Python packages required to run the application.

# Procfile

Used for deployment with platforms such as Heroku and specifies the application's startup command.

Example:

web: gunicorn app:app

.gitignore

Prevents unnecessary files and folders from being tracked by Git.

# What I Learned

- Flask application structure
- Routing and URL handling
- Form processing
- File uploads
- Database integration
- Template rendering with Jinja2
- Basic deployment preparation

# Project Status

Completed as a beginner learning project to practice Flask web development fundamentals.

# Author
Rita Okam
