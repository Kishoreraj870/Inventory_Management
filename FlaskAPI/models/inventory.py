from datetime import datetime
from bson.objectid import ObjectId
from db import inventory_data
from db import product_data
from db import supplier_data
from db import sale_data

db = inventory_data()
product_db=product_data()
supplier_db = supplier_data()
sale_db = sale_data()

class Inventory:
    REORDER_THRESHOLD = 2
    @staticmethod
    def add_item(data):
        product_id = data.get('product_id')
        if not product_id:
            raise ValueError("Product ID is required to add inventory")
        
        # Verify that the product exists in the Product collection
        product = product_db.product_data.find_one({'_id': ObjectId(product_id)})
        if not product:
            raise ValueError("Invalid Product ID. Product does not exist.")
        
        new_item = {
            'name': data['name'],
            'quantity': int(data['quantity']),
            'price': data['price'],
            'category': data.get('category', product.get('category', '')),
            'supplier': data.get('supplier', product.get('supplier', '')),
            'product_id': ObjectId(product_id)  # Store product_id as ObjectId
        }
        result = db.inventory.insert_one(new_item)
        return str(result.inserted_id)
    
    @staticmethod
    def get_all_items():
        items = db.inventory.find()
        return [{
            'id': str(item['_id']),
            'name': item['name'],
            'quantity': item['quantity'],
            'price': item['price'],
            'category': item.get('category', ''),
            'supplier': item.get('supplier', '')
        } for item in items]
    @staticmethod
    def get_item_by_id(item_id):
        item = db.inventory.find_one({'_id': ObjectId(item_id)})
        if item:
            return {
                'id': str(item['_id']),
                'name': item['name'],
                'quantity': item['quantity'],
                'price': item['price'],
                'category': item.get('category', ''),
                'supplier': item.get('supplier', '')
            }
        else:
            raise ValueError("Item not found") 
    
    @staticmethod
    def edit_item(item_id,data):
        updated_fields = {key: value for key, value in data.items() if value}
        result = db.inventory.update_one({'_id':ObjectId(item_id)}, {'$set': updated_fields})
        if result.modified_count == 0:
            raise ValueError("No changes made to the inventory item.")
        updated_item = db.inventory.find_one({'_id':ObjectId(item_id)})
        if updated_item and '_id' in updated_item:
            updated_item = str(updated_item)
        return updated_item
    
    @staticmethod
    def delete_item(item_id):
        result = db.inventory.delete_one({'_id':ObjectId(item_id)})
        if result.deleted_count == 0:
            raise ValueError("Item not found or already deleted.")
        
    @staticmethod
    def check_reorder_levels():
        items_below_threshold = db.inventory.find({'quantity': {'$lt': Inventory.REORDER_THRESHOLD}})
        return [{
            'id': str(item['_id']),
            'name': item['name'],
            'quantity': item['quantity'],
            'reorder_threshold': Inventory.REORDER_THRESHOLD
        } for item in items_below_threshold]   
         
class Product:
    @staticmethod
    def add_product(data):
        new_product = {
            'name' : data['name'],
            'description': data.get('description', ''), 
            'price': data['price'],
            'category' : data['category'],
            'supplier' : data.get('supplier','')
        }
        result = product_db.product_data.insert_one(new_product)
        return str(result.inserted_id)
    
    @staticmethod
    def product_list():
        return list(product_db.product_data.find())
    
    @staticmethod
    def get_product_by_id(product_id):
        product = product_db.product_data.find_one({'_id': ObjectId(product_id)})
        if product:
            return {
                'id': str(product['_id']),
                'name': product['name'],
                'description': product.get('description', ''),
                'price': product['price'],
                'category': product['category'],
                'supplier': product.get('supplier', '')
            }
        else:
            raise ValueError("Product not found")

    @staticmethod
    def edit_product(product_id, data):
        updated_fields = {key: value for key, value in data.items() if value}
        result = product_db.product_data.update_one({'_id': ObjectId(product_id)}, {'$set': updated_fields})
        if result.modified_count == 0:
            raise ValueError("No changes made to the product.")
        updated_product = product_db.product_data.find_one({'_id':ObjectId(product_id)})
        if updated_product and '_id' in updated_product:
            updated_product['_id'] = str(updated_product) 
        return updated_product

    @staticmethod
    def delete_product(product_id):
        result = product_db.product_data.delete_one({'_id': ObjectId(product_id)})
        if result.deleted_count == 0:
            raise ValueError("Product not found or already deleted.")

class Supplier:
    @staticmethod
    def add_supplier(data):
        new_supplier = {
            'name': data['name'],           # Supplier name
            'phone': data.get('phone', ''),  # Supplier contact number
            'email': data.get('email', ''),  # Supplier email address
            'address': data.get('address', '')  # Supplier's physical address
        }
        result = supplier_db.supplier_data.insert_one(new_supplier)
        return str(result.inserted_id)

    @staticmethod
    def get_all_suppliers():
        return list(supplier_db.supplier_data.find())

    @staticmethod
    def get_supplier_by_id(supplier_id):
        supplier = supplier_db.supplier_data.find_one({'_id': ObjectId(supplier_id)})
        if supplier:
            return {
                'id': str(supplier['_id']),
                'name': supplier['name'],
                'phone': supplier.get('phone', ''),
                'email': supplier.get('email', ''),
                'address': supplier.get('address', '')
            }
        else:
            raise ValueError("Supplier not found")

    @staticmethod
    def edit_supplier(supplier_id, data):
        updated_fields = {key: value for key, value in data.items() if value}
        result = supplier_db.supplier_data.update_one({'_id':ObjectId(supplier_id)}, {'$set': updated_fields})
        if result.modified_count == 0:
            raise ValueError("No changes made to the supplier.")
        updated_supplier = supplier_db.supplier_data.find_one({'_id': ObjectId(supplier_id)})
        if updated_supplier and '_id' in updated_supplier:
            updated_supplier['_id'] = str(updated_supplier['_id'])
        return updated_supplier

    @staticmethod
    def delete_supplier(supplier_id):
        result = supplier_db.supplier_data.delete_one({'_id': ObjectId(supplier_id)})
        if result.deleted_count == 0:
            raise ValueError("Supplier not found or already deleted.")

class Sale:
    @staticmethod
    def record_sale(data):
        product_id = ObjectId(data['product_id'])
        quantity = int(data['quantity']) 
        # print(type(product_id))
         # Check if there is enough stock
        product_in_inventory = db.inventory.find_one({'product_id': product_id})
    
        
        if product_in_inventory:
             # Ensure that the quantity in the inventory is treated as an integer
            inventory_quantity = int(product_in_inventory['quantity'])
            
            # Debugging prints
            print(f"Inventory quantity: {inventory_quantity} (type: {type(inventory_quantity)})")
            print(f"Requested quantity: {quantity} (type: {type(quantity)})")
            if inventory_quantity >= quantity:
                
                sale = {
                'product_id': ObjectId(data['product_id']),  # Link to Product
                'quantity': data['quantity'],               # Quantity sold
                'sale_price': data['sale_price'],           # Sale price per unit
                'sale_date': data.get('sale_date', datetime.utcnow())  # Date of sale
                }
                
                # Reduce quantity from Inventory
                db.inventory.update_one(
                    {'product_id': sale['product_id']},
                    {'$inc': {'quantity': -quantity}}
                )
                
                result = sale_db.sales_data.insert_one(sale)
                return str(result.inserted_id)
            else:
                raise ValueError("Insufficient stock to complete the sale.")
            
        else:
            raise ValueError("Insufficient stock to complete the sale.")

    @staticmethod
    def get_all_sales():
        return list(sale_db.sales_data.find())
    
    @staticmethod
    def get_sale_by_id(sale_id):
        sale = sale_db.sales_data.find_one({'_id': ObjectId(sale_id)})
        if sale:
            return {
                'id': str(sale['_id']),
                'product_id': str(sale['product_id']),
                'quantity': sale['quantity'],
                'sale_price': sale['sale_price'],
                'sale_date': sale.get('sale_date', '')
            }
        else:
            raise ValueError("Sale not found")

    @staticmethod
    def edit_sale(sale_id, data):
        updated_fields = {key: value for key, value in data.items() if value}
        result = sale_db.sales_data.update_one({'_id': ObjectId(sale_id)}, {'$set': updated_fields})
        if result.modified_count == 0:
            raise ValueError("No changes made to the sale.")
        updated_sale = sale_db.sales_data.find_one({'_id': ObjectId(sale_id)})
        if updated_sale and '_id' in updated_sale:
            updated_sale['_id'] = str(updated_sale['_id'])
        return updated_sale

    @staticmethod
    def delete_sale(sale_id):
        result = sale_db.sales_data.delete_one({'_id': ObjectId(sale_id)})
        if result.deleted_count == 0:
            raise ValueError("Sale not found or already deleted.")
        
    @staticmethod
    def generate_bill(sale_id):
        sale = sale_db.sales_data.find_one({'_id': ObjectId(sale_id)})
        if not sale:
            raise ValueError("Sale not found")

        # Here you can format the bill as needed
        bill = {
            'product_id': str(sale['product_id']),
            'quantity': sale['quantity'],
            'sale_price': sale['sale_price'],
            'total_price': int(sale['quantity']) * int(sale['sale_price']),
            'sale_date': sale['sale_date'],
        }
        return bill
