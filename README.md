BloglicApp - Blogging Simplified
A Comprehensive blogging application built with Django, allowing users to create, edit, and delete blog posts, as well as comment and like their blog posts.

Features
1. User authentication using Django's built-in authentication system
2. Blog post model with title, content, author, created_at, updated_at, and status fields
3. Views and templates for listing, creating, updating, deleting, and viewing blog posts
4. Comment model with post, author, content, and created_at fields
5. Views and templates for adding and displaying comments
6. Like functionality with a like button and tracking of likes for each post


Requirements
Django 3.2+
Python 3.8+

Installation
Clone the repository: git clone https://github.com/AayushMore1708/Bloglic.git
Navigate to the project directory: cd Bloglic
Install dependencies: pip install -r requirements.txt
Run migrations: py manage.py makemigrations BloglicApp
                py manage.py migrate
Run the development server: py manage.py runserver

