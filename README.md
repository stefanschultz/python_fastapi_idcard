# FastAPI ID Card Management Application
FastAPI ID Card Management System: A sleek and efficient RESTful API service built with FastAPI for creating, managing, and deleting ID cards. This project showcases the power of Python's async capabilities and type hinting, offering CRUD operations (Create, Read, Update, Delete) with a clean, intuitive interface. Designed for ease of use and rapid development, it includes detailed endpoint documentation and examples for quick integration and testing. Dive into the world of modern web API development with our fully-documented, open-source project!


## Start the Application
Install the required dependencies using pip:
```
pip install -r requirements.txt
```
Run the FastAPI application using the following command:
```
uvicorn main:app --reload
```
The application will start on http://localhost:8000 by default.


## Endpoints Overview
- Create an ID Card: POST /id-cards/
- Get an ID Card: GET /id-cards/{id_card_id}
- List All ID Cards: GET /id-cards/
- Update an ID Card: PUT /id-cards/{id_card_id}
- Delete an ID Card: DELETE /id-cards/{id_card_id}

## Usage Examples
### Create an ID Card
To create a new ID card, send a POST request with the required details.
```
POST /id-cards/
Content-Type: application/json

{
    "first_name": "Jane",
    "last_name": "Doe",
    "birth_date": "1990-01-01",
    "expiration_date": "2030-01-01",
    "is_active": true
}
```

### Get an ID Card
Retrieve details of an ID card by its unique identifier.
```
GET /id-cards/{card_id}
```
Replace {id_card_id} with the actual ID of the ID card.

### List All ID Cards
List details of all ID cards.
```
GET /id-cards/
```

### Update an ID Card
Update details of an existing ID card by its ID.
```
PUT /id-cards/{card_id}
Content-Type: application/json

{
    "first_name": "Jane",
    "last_name": "Doe Updated",
    "birth_date": "1990-01-01",
    "expiration_date": "2030-01-01",
    "is_active": true
}
```
Replace {id_card_id} with the ID of the ID card you want to update.

### Delete an ID Card
Delete an ID card by its unique identifier.
```
DELETE /id-cards/{card_id}
```
Replace {id_card_id} with the ID of the ID card you wish to delete.


### Get storage type
Retrieve the storage type of the application
```
GET /storage-type/
```
The result will be a JSON object with the storage type.
Storage type can be either "in-memory", "redis".
As example, if the storage type is "in-memory", the result will be:
```
{
    "storage_type": "in-memory"
}
```