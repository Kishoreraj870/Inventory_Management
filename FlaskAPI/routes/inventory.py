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

@bp.route('/inventory/<id>', methods=['GET'])
def get_inventory_item(id):
    try:
        item = Inventory.get_item_by_id(id)
        return jsonify(item), 200
    except ValueError as e:
        return jsonify({'error': str(e)}), 400

@bp.route('/inventory/<id>', methods=['PUT'])
def edit_inventory(id):
    data = request.get_json()
    try:
        updated_item = Inventory.edit_item(id,data)
        return jsonify(updated_item)
    except ValueError as e:
        return jsonify({'error':str(e)})
    
@bp.route('/inventory/<id>',methods=['DELETE'])
def delete_inventory(id):
    try:
        Inventory.delete_item(id)
        return jsonify({"message": "Inventory item deleted"}), 200
    except ValueError as e:
        return jsonify({"error": str(e)}), 400
        

@bp.route('/inventory/reorder-alerts', methods=['GET'])
def get_reorder_alerts():
    items = Inventory.check_reorder_levels()
    return jsonify(items), 200

@pro.route('/product',methods=['POST'])
def add_product():
    data = request.get_json()
    product_id = Product.add_product(data)
    return jsonify({'id':product_id}), 201

@pro.route('/product/<id>', methods=['GET'])
def get_product_item(id):
    try:
        product = Product.get_product_by_id(id)
        return jsonify(product), 200
    except ValueError as e:
        return jsonify({'error': str(e)}), 400


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
 
@pro.route('/product/<id>', methods=['PUT'])
def edit_product(id):
    data = request.get_json()
    updated_product = Product.edit_product(id, data)
    return jsonify(updated_product), 200

# Delete Product
@pro.route('/product/<id>', methods=['DELETE'])
def delete_product(id):
    try:
        Product.delete_product(id)
        return jsonify({"message": "Product deleted"}), 200
    except ValueError as e:
        return jsonify({"error": str(e)}), 400
    
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

@supplier_route.route('/supplier/<id>', methods=['GET'])
def get_supplier_item(id):
    try:
        supplier = Supplier.get_supplier_by_id(id)
        return jsonify(supplier), 200
    except ValueError as e:
        return jsonify({'error': str(e)}), 400


# Edit Supplier
@supplier_route.route('/supplier/<id>', methods=['PUT'])
def edit_supplier(id):
    data = request.get_json()
    updated_supplier = Supplier.edit_supplier(id, data)
    return jsonify(updated_supplier), 200

# Delete Supplier
@supplier_route.route('/supplier/<id>', methods=['DELETE'])
def delete_supplier(id):
    try:
        Supplier.delete_supplier(id)
        return jsonify({"message": "Supplier deleted"}), 200
    except ValueError as e:
        return jsonify({"error": str(e)}), 400

@sale_route.route('/sale',methods=['POST'])
def add_sale():
    try:
        data = request.get_json()
        sale_id = Sale.record_sale(data)
        return jsonify({'id': sale_id}), 201
    except ValueError as e:
        return jsonify({'error': str(e)}), 400
    except Exception as e:
        print(e)
        return jsonify({'error': 'An error occurred while recording sale'}), 500

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
    
@sale_route.route('/sale/<id>', methods=['GET'])
def get_sale_item(id):
    try:
        sale = Sale.get_sale_by_id(id)
        return jsonify(sale), 200
    except ValueError as e:
        return jsonify({'error': str(e)}), 400

    
# Edit Sale
@sale_route.route('/sale/<id>', methods=['PUT'])
def edit_sale(id):
    data = request.get_json()
    updated_sale = Sale.edit_sale(id, data)
    return jsonify(updated_sale), 200

# Delete Sale
@sale_route.route('/sale/<id>', methods=['DELETE'])
def delete_sale(id):
    try:
        Sale.delete_sale(id)
        return jsonify({"message": "Sale deleted"}), 200
    except ValueError as e:
        return jsonify({"error": str(e)}), 400
