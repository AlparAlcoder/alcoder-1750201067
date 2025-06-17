# Documentation for FastAPI Based API

This API is developed using FastAPI and Pydantic. It provides two endpoints - one for creating an item and another for retrieving an item by its name.

## FastAPI Endpoints

There are two main endpoints:

- POST `/items/`
- GET `/items/{item_name}`

### POST `/items/`

This endpoint is used to create a new item.

#### Parameters

- `item: Item` (required): a JSON object that describes the item. The object should be in the format of the `Item` model.

#### Response

Returns the created `Item` object.

#### Errors

- `400 Bad Request`: if the item already exists.

#### Example

```bash
curl -X POST -H "Content-Type: application/json" -d '{"name": "item1", "description": "This is item 1", "price": 10.0}' http://localhost:8000/items/
```

### GET `/items/{item_name}`

This endpoint is used to retrieve an item by its name.

#### Parameters

- `item_name: str` (required): the name of the item.

#### Response

Returns the `Item` object associated with `item_name`.

#### Errors

- `404 Not Found`: if the item does not exist.

#### Example

```bash
curl -X GET http://localhost:8000/items/item1
```

## Pydantic Models

There is one Pydantic model:

- `Item`

### Item

The `Item` model validates the data of the item. It has three properties:

- `name: str`: the name of the item.
- `description: str`: the description of the item.
- `price: float`: the price of the item.

## Important Notes

- The `Item` model does not permit extra attributes. Therefore, the JSON object in the POST request should only contain `name`, `description`, and `price`.
- The item names are case-sensitive.
- The item names must be unique.

## Dependencies

- Python 3.6+
- FastAPI
- Pydantic
- Uvicorn (for serving the application)
