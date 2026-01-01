Contributor Clarification 
This repository shows contributions from two GitHub accounts: 
@jaylerjackson (Richard Sam Jackson) 
@iamjaylerjackson (Jayler Jackson) 

Both accounts belong to the same person (me). 

I was unable to connect my original GitHub account to ALX for this course because it had already been linked to a previous ALX program (ALX AICE – AI Essentials) using a different email address. As a result, I created a new GitHub account for this project. During development, I made commits from both accounts without realizing it, which is why GitHub lists them as separate contributors. No external assistance was involved in building this project.

Car Rental Backend API

By Richard Sam Jackson

This project is a car rental backend API built as part of my ALX backend web development capstone project.
The goal is to build a secure and scalable backend system for managing cars and rentals.

What I was able to complete so far

1. Created and configured a Django REST framework project
2. Connected the project to a MySQL database and successfully ran migrations
3. Implemented JWT authentication using Django SimpleJWT
4. Successfully tested login and protected endpoints using Thunder Client

Challenges faced and how I handled them

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
