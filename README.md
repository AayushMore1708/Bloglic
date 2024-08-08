Bloglic
A simple blog application built with Django, allowing users to create, edit, and delete blog posts, as well as comment and like posts.

Features
User authentication using Django's built-in authentication system
Blog post model with title, content, author, created_at, updated_at, and status fields
Views and templates for listing, creating, updating, deleting, and viewing blog posts
Comment model with post, author, content, and created_at fields
Views and templates for adding and displaying comments
Like functionality with a like button and tracking of likes for each post
Requirements
Django 3.2+
Python 3.8+
Installation
Clone the repository: git clone https://github.com/your-username/Bloglic.git
Navigate to the project directory: cd Bloglic
Install dependencies: pip install -r requirements.txt
Run migrations: python manage.py migrate
Run the development server: python manage.py runserver
Usage
Register a new user account by visiting http://localhost:8000/register/
Log in to your account by visiting http://localhost:8000/login/
Create a new blog post by visiting http://localhost:8000/posts/create/
View all blog posts by visiting http://localhost:8000/posts/
View a single blog post by visiting http://localhost:8000/posts/<post_id>/
Add a comment to a blog post by visiting http://localhost:8000/posts/<post_id>/comment/
Like a blog post by clicking the like button on the post's page
