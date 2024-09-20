# Add this to your app.py for managing inventory
from bson.objectid import ObjectId
from flask import jsonify, request, Blueprint
from models.inventory import Inventory
from models.inventory import Product
from models.inventory import Supplier
from models.inventory import Sale

bp = Blueprint('inventory',__name__)
pro = Blueprint('product', __name__)
supplier_route = Blueprint('supplier', __name__)
sale_route = Blueprint('sale', __name__)


@bp.route('/inventory',methods=['POST'])
def add_inventory():
    data = request.get_json()
    item_id = Inventory.add_item(data)
    return jsonify({'id':item_id}),201

@bp.route('/inventory',methods=['GET'])
def get_inventory():
    items = Inventory.get_all_items()
    return jsonify(items),200

@pro.route('/product',methods=['POST'])
def add_product():
    data = request.get_json()
    product_id = Product.add_product(data)
    return jsonify({'id':product_id}), 201

@pro.route('/product',methods=['GET'])
def get_product():
    try:
        # Fetch items from the database
        items = list(Product.product_list())
        
        # Convert ObjectId to string for each item
        for item in items:
            item['_id'] = str(item['_id'])
        
        return jsonify(items), 200  # Return the modified items as JSON
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({"error": "An error occurred while fetching products"}), 500
 
 
@supplier_route.route('/supplier',methods=['POST'])
def add_supplier():
    data = request.get_json()
    supplier_id = Supplier.add_supplier(data)
    return jsonify({'id':supplier_id}), 201

@supplier_route.route('/supplier',methods=['GET'])
def get_supplier():
    try:    
        items = list(Supplier.get_all_suppliers())
        for item in items:
            item['_id'] = str(item['_id'])
        return jsonify(items),200   
    except Exception as e:
        print(f"Error:{e}")
        return jsonify({"error": "An error occurred while fetching products"}), 500


@sale_route.route('/sale',methods=['POST'])
def add_sale():
    data = request.get_json()
    sale_id = Sale.record_sale(data)
    return jsonify({'id':sale_id}), 201

@sale_route.route('/sale',methods=['GET'])
def get_sale():
    try:
        items = list(Sale.get_all_sales())
        for item in items:
            item['_id'] = str(item['_id'])
            item['product_id'] = str(item['product_id']) 
        return jsonify(items),200   
    except Exception as e:
        print(f"Error:{e}")
        return jsonify({"error":"An error occured while fetchoing sale"}),500
