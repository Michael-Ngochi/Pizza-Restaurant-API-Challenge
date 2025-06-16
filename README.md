# Pizza Restaurant API Challenge

## Project Overview

A simple RESTful API for managing restaurants, pizzas, and restaurant-pizza relationships built with:

- Flask
- Flask SQLAlchemy
- Flask Migrate
- SQLite
- Postman for testing

## Repository

[GitHub Repository](https://github.com/Michael-Ngochi/Pizza-Restaurant-API-Challenge.git)

## Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/Michael-Ngochi/Pizza-Restaurant-API-Challenge.git
cd Pizza-Restaurant-API-Challenge
```

### 2. Install dependencies

```bash
pipenv install
pipenv shell
```

Alternatively, you can use a standard virtual environment:

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 3. Set environment variables

If using Flask CLI:

```bash
export FLASK_APP=server.app
export FLASK_ENV=development
```

Or create a `.flaskenv` file at project root:

```bash
FLASK_APP=server.app
FLASK_ENV=development
```

## Database Setup

### 1. Initialize migrations (only once)

```bash
flask db init
```

### 2. Generate migration

```bash
flask db migrate -m "Initial models"
```

### 3. Apply migration

```bash
flask db upgrade
```

### 4. Seed the database

```bash
python -m server.seed
```

This loads sample Kenyan restaurants and pizzas.

## Project Structure

```
server/
  app.py
  config.py
  __init__.py
  models/
    __init__.py
    restaurant.py
    pizza.py
    restaurant_pizza.py
  controllers/
    __init__.py
    restaurant_controller.py
    pizza_controller.py
    restaurant_pizza_controller.py
  seed.py
migrations/
challenge-1-pizzas.postman_collection.json
README.md
```

## Routes Summary

| Method | Endpoint      | Description         |
| ------ | ------------- | ------------------- |
| GET    | /restaurants/ | Get all restaurants |
| GET    | /restaurants/ |                     |

| [int\:id](int\:id) | Get restaurant details with pizzas |                                     |
| ------------------ | ---------------------------------- | ----------------------------------- |
| DELETE             | /restaurants/[int\:id](int\:id)    | Delete a restaurant and its pizzas  |
| GET                | /pizzas/                           | Get all pizzas                      |
| POST               | /restaurant\_pizzas/               | Create restaurant-pizza association |

## Example Requests & Responses

### GET /restaurants

Response:

```json
[
  {
    "id": 1,
    "name": "Pizza Inn",
    "address": "Westlands, Nairobi"
  }
]
```

### GET /restaurants/[int\:id](int\:id)

Response:

```json
{
  "id": 1,
  "name": "Pizza Inn",
  "address": "Westlands, Nairobi",
  "pizzas": [
    {
      "id": 1,
      "name": "Chicken Tikka",
      "ingredients": "Chicken Tikka, Mozzarella, Onions, Green Pepper"
    }
  ]
}
```

If not found:

```json
{ "error": "Restaurant not found" }
```

### DELETE /restaurants/[int\:id](int\:id)

Response:

- 204 No Content (successful)
- 404 with `{ "error": "Restaurant not found" }` if invalid ID

### GET /pizzas

Response:

```json
[
  {
    "id": 1,
    "name": "Chicken Tikka",
    "ingredients": "Chicken Tikka, Mozzarella, Onions, Green Pepper"
  }
]
```

### POST /restaurant\_pizzas

Request:

```json
{
  "price": 5,
  "pizza_id": 1,
  "restaurant_id": 3
}
```

Success Response:

```json
{
  "id": 4,
  "price": 5,
  "pizza_id": 1,
  "restaurant_id": 3,
  "pizza": {
    "id": 1,
    "name": "Chicken Tikka",
    "ingredients": "Chicken Tikka, Mozzarella, Onions, Green Pepper"
  },
  "restaurant": {
    "id": 3,
    "name": "Domino's Pizza",
    "address": "Galleria Mall, Nairobi"
  }
}
```

Validation Error Response:

```json
{
  "errors": ["Price must be between 1 and 30"]
}
```

## Validation Rules

- price must be between 1 and 30 for RestaurantPizza.
- If missing required fields, returns 400 with appropriate error message.

## Postman Usage

### 1. Import Postman collection

File: `challenge-1-pizzas.postman_collection.json`\
Import directly in Postman.

### 2. Set base URL

The collection uses:

```
http://127.0.0.1:5000/
```

### 3. Available requests in Postman

- GET /restaurants/
- GET /restaurants/\:id
- DELETE /restaurants/\:id
- GET /pizzas/
- POST /restaurant\_pizzas/

