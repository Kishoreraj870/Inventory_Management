Overview
This API provides endpoints for managing an inventory system, allowing users to add, retrieve, update, and delete records for inventory items, products, suppliers, and sales.

Base URL
The base URL for accessing the API endpoints is http://<host>:<port>/.

Endpoints
Inventory Management
Add Inventory Item
Endpoint: /inventory
Method: POST
Request Body: JSON object containing inventory item data.
Response:
201 Created: Returns the ID of the newly created inventory item.
Example:
json
Copy code
{
  "id": "60a1f1e3f1a2c0d3b12f6d3e"
}
Get All Inventory Items
Endpoint: /inventory
Method: GET
Response:
200 OK: Returns a list of all inventory items.
Example:
json
Copy code
[
  {
    "_id": "60a1f1e3f1a2c0d3b12f6d3e",
    "name": "Item A",
    "quantity": 100
  },
  ...
]
Get Inventory Item by ID
Endpoint: /inventory/<id>
Method: GET
Response:
200 OK: Returns the details of the specified inventory item.
400 Bad Request: If the item ID is invalid.
Example:
json
Copy code
{
  "_id": "60a1f1e3f1a2c0d3b12f6d3e",
  "name": "Item A",
  "quantity": 100
}
Edit Inventory Item
Endpoint: /inventory/<id>
Method: PUT
Request Body: JSON object containing updated inventory item data.
Response:
200 OK: Returns the updated inventory item details.
400 Bad Request: If the item ID is invalid or update fails.
Example:
json
Copy code
{
  "_id": "60a1f1e3f1a2c0d3b12f6d3e",
  "name": "Updated Item A",
  "quantity": 150
}
Delete Inventory Item
Endpoint: /inventory/<id>
Method: DELETE
Response:
200 OK: Confirms that the inventory item has been deleted.
400 Bad Request: If the item ID is invalid.
Example:
json
Copy code
{
  "message": "Inventory item deleted"
}
Get Reorder Alerts
Endpoint: /inventory/reorder-alerts
Method: GET
Response:
200 OK: Returns a list of items that need to be reordered.
Example:
json
Copy code
[
  {
    "_id": "60a1f1e3f1a2c0d3b12f6d3e",
    "name": "Item B",
    "quantity": 10
  },
  ...
]
Product Management
Add Product
Endpoint: /product
Method: POST
Request Body: JSON object containing product data.
Response:
201 Created: Returns the ID of the newly created product.
Example:
json
Copy code
{
  "id": "60a1f1e3f1a2c0d3b12f6d3f"
}
Get All Products
Endpoint: /product
Method: GET
Response:
200 OK: Returns a list of all products.
Example:
json
Copy code
[
  {
    "_id": "60a1f1e3f1a2c0d3b12f6d3f",
    "name": "Product A",
    "price": 20.5
  },
  ...
]
Get Product by ID
Endpoint: /product/<id>
Method: GET
Response:
200 OK: Returns the details of the specified product.
400 Bad Request: If the product ID is invalid.
Example:
json
Copy code
{
  "_id": "60a1f1e3f1a2c0d3b12f6d3f",
  "name": "Product A",
  "price": 20.5
}
Edit Product
Endpoint: /product/<id>
Method: PUT
Request Body: JSON object containing updated product data.
Response:
200 OK: Returns the updated product details.
Example:
json
Copy code
{
  "_id": "60a1f1e3f1a2c0d3b12f6d3f",
  "name": "Updated Product A",
  "price": 22.0
}
Delete Product
Endpoint: /product/<id>
Method: DELETE
Response:
200 OK: Confirms that the product has been deleted.
400 Bad Request: If the product ID is invalid.
Example:
json
Copy code
{
  "message": "Product deleted"
}
Supplier Management
Add Supplier
Endpoint: /supplier
Method: POST
Request Body: JSON object containing supplier data.
Response:
201 Created: Returns the ID of the newly created supplier.
Example:
json
Copy code
{
  "id": "60a1f1e3f1a2c0d3b12f6d4a"
}
Get All Suppliers
Endpoint: /supplier
Method: GET
Response:
200 OK: Returns a list of all suppliers.
Example:
json
Copy code
[
  {
    "_id": "60a1f1e3f1a2c0d3b12f6d4a",
    "name": "Supplier A",
    "contact": "1234567890"
  },
  ...
]
Get Supplier by ID
Endpoint: /supplier/<id>
Method: GET
Response:
200 OK: Returns the details of the specified supplier.
400 Bad Request: If the supplier ID is invalid.
Example:
json
Copy code
{
  "_id": "60a1f1e3f1a2c0d3b12f6d4a",
  "name": "Supplier A",
  "contact": "1234567890"
}
Edit Supplier
Endpoint: /supplier/<id>
Method: PUT
Request Body: JSON object containing updated supplier data.
Response:
200 OK: Returns the updated supplier details.
Example:
json
Copy code
{
  "_id": "60a1f1e3f1a2c0d3b12f6d4a",
  "name": "Updated Supplier A",
  "contact": "0987654321"
}
Delete Supplier
Endpoint: /supplier/<id>
Method: DELETE
Response:
200 OK: Confirms that the supplier has been deleted.
400 Bad Request: If the supplier ID is invalid.
Example:
json
Copy code
{
  "message": "Supplier deleted"
}
Sale Management
Add Sale
Endpoint: /sale
Method: POST
Request Body: JSON object containing sale data.
Response:
201 Created: Returns the ID of the newly recorded sale.
Example:
json
Copy code
{
  "id": "60a1f1e3f1a2c0d3b12f6d5b"
}
Get All Sales
Endpoint: /sale
Method: GET
Response:
200 OK: Returns a list of all sales records.
Example:
json
Copy code
[
  {
    "_id": "60a1f1e3f1a2c0d3b12f6d5b",
    "product_id": "60a1f1e3f1a2c0d3b12f6d3f",
    "quantity": 5,
    "total_price": 102.5
  },
  ...
]
Get Sale by ID
Endpoint: /sale/<id>
Method: GET
Response:
200 OK: Returns the details of the specified sale.
400 Bad Request: If the sale ID is invalid.
Example:
json
Copy code
{
  "_id": "60a1f1e3f1a2c0d3b12f6d5b",
  "product_id": "60a1f1e3f1a2c0d3b12f6d3f",
  "quantity": 5,
  "total_price": 102.5
}
Edit Sale
Endpoint: /sale/<id>
Method: PUT
Request Body: JSON object containing updated sale data.
Response:
200 OK: Returns the updated sale details.
Example:
json
Copy code
{
  "_id": "60a1f1e3f1a2c0d3b12f6d5b",
  "product_id": "60a1f1e3f1a2c0d3b12f6d3f",
  "quantity": 10,
  "total_price": 205.0
}
Delete Sale
Endpoint: /sale/<id>
Method: DELETE
Response:
200 OK: Confirms that the sale has been deleted.
400 Bad Request: If the sale ID is invalid.
Example:
json
Copy code
{
  "message": "Sale deleted"
}
Generate Bill
Endpoint: /sale/bill/<id>
Method: GET
Response:
200 OK: Returns the generated bill for the specified sale.
400 Bad Request: If the sale ID is invalid.
Example:
json
Copy code
{
  "bill_id": "60a1f1e3f1a2c0d3b12f6d5b",
  "total_amount": 102.5,
  "items": [
    {
      "product_name": "Product A",
      "quantity": 5,
      "price_per_item": 20.5
    }
  ]
}
Error Handling
Common error responses include:

400 Bad Request: Indicates that the request was invalid (e.g., invalid IDs).
500 Internal Server Error: Indicates that an unexpected error occurred on the server side.