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
    @staticmethod
    def add_item(data):
        new_item ={
            'name': data['name'],
            'quantity': data['quantity'],
            'price': data['price'],
            'category': data.get('category', ''),
            'supplier': data.get('supplier', ''),
            'product_id' : data.get('product_id')
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

class Sale:
    @staticmethod
    def record_sale(data):
        quantity = int(data['quantity']) 
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

    @staticmethod
    def get_all_sales():
        return list(sale_db.sales_data.find())
