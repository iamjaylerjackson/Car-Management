# Car-Management

Name: Richard Sam Jackson

Car Management

This is my inventory car management. I hope I do a great job on it.

What I have accomplished so far

Created and configured a Django REST Framework project
Connected the project to a MySQL database and ran migrations
Implemented JWT authentication using Django SimpleJWT
Successfully tested login and protected endpoints using Thunder Client

Challenges faced and how I handled them

Faced issues with HTTP methods and missing authorization headers during testing
Resolved them by using the correct request method (POST) and adding the Authorization header with a Bearer token

What’s next

Create core models for the Car Rental system (Cars, Rentals)
Build CRUD APIs for managing cars
Protect important endpoints using JWT authentication

{
"username": "kofi202",  
"email": "info.rsamjackson@gmail.com",
"password": "Password$2025"
}

http://127.0.0.1:8000/api/auth/login/

http://127.0.0.1:8000/api/protected/

{
"name": "Corolla",
"brand": "Toyota",
"model_year": 2022,
"license_plate": "GT-5566-24",
"category": "sedan",
"price_per_day": "500",
"status": "available",
}

{
"username": "kofi202",
"email": "kofi202@gmail.com",
"password": "TryOutpass2026"
}
