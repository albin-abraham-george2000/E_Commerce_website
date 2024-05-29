# E-Commerce Website

This is a fully functional e-commerce website built using the Django web framework. The application allows users to browse products, add them to a shopping cart, and proceed to checkout.

# Features
+ User authentication (register, login, logout)

+ Product browsing by categories

+ Product search functionality
+ Shopping cart management
+ Order processing and checkout
+ Payment integration (e.g., Stripe, PayPal)
+ Admin panel for managing products, orders, and users

# Technologies Used
+ Django
+ HTML/CSS
+ javaScript
+ SQLite (for Development)
+ PostgreSQL 
+ Stripe (for Payment)
 # Project Structure

ecommerce/
├── ecommerce/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   ├── asgi.py
│   └── ...
├── products/
│   ├── migrations/
│   ├── templates/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── views.py
│   └── ...
├── cart/
│   ├── migrations/
│   ├── templates/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── views.py
│   └── ...
├── orders/
│   ├── migrations/
│   ├── templates/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── views.py
│   └── ...
├── users/
│   ├── migrations/
│   ├── templates/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── views.py
│   └── ...
├── manage.py
└── requirements.txt
