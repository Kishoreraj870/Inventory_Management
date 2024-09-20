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
    items = Product.product_list()
    return jsonify(items),200
 
 
@supplier_route.route('/supplier',methods=['POST'])
def add_supplier():
    data = request.get_json()
    supplier_id = Supplier.add_supplier(data)
    return jsonify({'id':supplier_id}), 201

@supplier_route.route('/supplier',methods=['GET'])
def get_supplier():
    items = Supplier.get_all_suppliers()
    return jsonify(items),200   


@sale_route.route('/sale',methods=['POST'])
def add_sale():
    data = request.get_json()
    sale_id = Sale.record_sale(data)
    return jsonify({'id':sale_id}), 201

@sale_route.route('/sale',methods=['GET'])
def get_sale():
    items = Sale.get_all_sales()
    return jsonify(items),200   
