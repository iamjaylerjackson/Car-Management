Car Rental Backend API

By Richard Sam Jackson

This project is a car rental backend API built as part of my ALX backend web development capstone project.
The goal is to build a secure and scalable backend system for managing cars and rentals.

What i was able to complate so far

1. Created and configured a Django REST framework project
2. Connected the project to a MySQL database and successfully ran migrations
3. Implemented JWT authentication using Django SimpleJWT
4. Successfully tested login and protected endpoints using Thunder Client

Challenges faced and how i handled them

Faced issues with incorrect HTTP methods and missing authorization headers during testing

Resolved by:

1. Using the correct request methods
2. Adding the Authorization: Bearer token header for protected endpoints

What's next after the capstone project

1. Create core models for the car rental system (Cars, Rentals)
2. Build CRUD APIs for managing cars
3. Protect sensitive endpoints using JWT authentication
4. Continue testing endpoints using Thunder Client

Sample API Endpoints
Login:
POST /api/auth/login/
Protected test endpoint:
GET /api/protected/
