# Todo-List-API

This is a Flask-based RESTful API for managing a Todo List. You can create an account, log in, and manage your todos (create, update, get, delete). The project uses MySQL as the database for storing users and todo items.

## Prerequisites

- Python 3.9+
- Flask and required dependencies
- MySQL Database
- Postman for API testing

## Setup Instructions

1.	Clone the Repository
2.	Create a Virtual Environment
3.	Install Dependencies
4.	Run the Application ( ⚠️ The application will be running at http://127.0.0.1:5000. For local development only. If deploying to production, replace this with your server's URL)

## Using Postman to Test the API

1. Register a User
-	Method: POST
-	URL: http://127.0.0.1:5000/auth/register
-	Headers:
    - `Content-Type: application/json`
-	Body (raw JSON):
```
{
  "username": "your_username",
  "password": "your_password"
}
```
-	Result: If successful, you will receive a 201 Created response with a token.
  
2. Log in
-	Method: POST
-	URL: http://127.0.0.1:5000/auth/login
-	Headers:
    - `Content-Type: application/json`
-	Body (raw JSON):
```
{
  "username": "your_username",
  "password": "your_password"
}
```
-	Result: If successful, you will receive a 200 OK response with a token. Save this token for subsequent requests.
  
3. Create a Todo Item
-	Method: POST
-	URL: http://127.0.0.1:5000/api/todos
-	Headers:
    - `Content-Type: application/json`
    - `Authorization: Bearer <your_token> (replace <your_token> with the token from login)`
-	Body (raw JSON):
```
{
  "title": "Your Todo Title",
  "description": "Your Todo Description"
}
```
-	Result: If successful, you will receive a 201 Created response with the new todo item.
  
4. Get All Todo Items
-	Method: GET
-	URL: http://127.0.0.1:5000/api/todos
-	Headers:
    - `Authorization: Bearer <your_token>`
-	Result: If successful, you will receive a 200 OK response with a list of all your todo items.
  
5. Update a Todo Item
-	Method: PUT
-	URL: http://127.0.0.1:5000/api/todos/<todo_id> (replace <todo_id> with the ID of the todo you want to update)
-	Headers:
    - `Content-Type: application/json`
    - `Authorization: Bearer <your_token>`
-	Body (raw JSON):
```
{
  "title": "Updated Todo Title",
  "description": "Updated Todo Description"
}
```
-	Result: If successful, you will receive a 200 OK response with the updated todo item.
  
6. Delete a Todo Item
-	Method: DELETE
-	URL: http://127.0.0.1:5000/api/todos/<todo_id> (replace <todo_id> with the ID of the todo you want to delete)
-	Headers:
    - `Authorization: Bearer <your_token>`
-	Result: If successful, you will receive a 204 No Content response, indicating the item was deleted.



