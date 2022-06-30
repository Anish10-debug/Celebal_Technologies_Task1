# INTRODUCTION
Student Application using FastAPI framework having the following functionality.
1. API to sign up
2. API to check authentication
3. API to fetch all student records
4. API to fetch student records by id
5. API to insert student records
6. API to update student record by id
7. API to delete a student record by id

Database used is MySQL. User has to sign up first and after signing up the hashed password will be stored in mysql using bcrypt from passlib password hashing library.
After getting authenticated a JWT token will be returned and then the user can use all the REST endpoints (GET/POST/PUT/DELETE) and explore the above mentioned 
functionalities.
