Overview
A system for managing products, suppliers, inventory items, and sales.
Built using Python and MongoDB.
Provides functionalities for adding, editing, retrieving, and deleting records.
Prerequisites
Python: Version 3.x
MongoDB: Installed and running.
Python Libraries: bson, datetime
Directory Structure
db.py: Database connection and configuration.
inventory.py: Main classes for inventory management (Inventory, Product, Supplier, Sale).
README.md: Documentation file.
Setup
Clone or download the repository.
Ensure MongoDB is running.
Install required Python libraries if not already installed.
Classes and Methods
Inventory Class
add_item(data): Adds a new inventory item.
get_all_items(): Retrieves all inventory items.
get_item_by_id(item_id): Retrieves an item by ID.
edit_item(item_id, data): Edits an existing item.
delete_item(item_id): Deletes an item from inventory.
check_reorder_levels(): Checks items below reorder threshold.
Product Class
add_product(data): Adds a new product.
product_list(): Retrieves all products.
get_product_by_id(product_id): Retrieves a product by ID.
edit_product(product_id, data): Edits an existing product.
delete_product(product_id): Deletes a product.
Supplier Class
add_supplier(data): Adds a new supplier.
get_all_suppliers(): Retrieves all suppliers.
get_supplier_by_id(supplier_id): Retrieves a supplier by ID.
edit_supplier(supplier_id, data): Edits an existing supplier.
delete_supplier(supplier_id): Deletes a supplier.
Sale Class
record_sale(data): Records a new sale and updates inventory.
get_all_sales(): Retrieves all sales records.
get_sale_by_id(sale_id): Retrieves a sale by ID.
edit_sale(sale_id, data): Edits an existing sale.
delete_sale(sale_id): Deletes a sale.
generate_bill(sale_id): Generates a bill for a specific sale.
Usage Examples
Adding a Product:

python
Copy code
product_data = {...}  # Product details
product_id = Product.add_product(product_data)
Recording a Sale:

python
Copy code
sale_data = {...}  # Sale details
sale_id = Sale.record_sale(sale_data)
Error Handling
Raises ValueError for:
Missing required fields.
Invalid IDs or item not found.
Insufficient stock for sales.