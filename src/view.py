from flask import Flask, request, jsonify
from flask_restful import Resource, abort
from . import models
#init schema
product_schema = models.ProductSchema(strict=False)
products_schema = models.ProductSchema(many=True, strict=False)

def try_error(id):
    if not models.Product.query.get(id):
        abort(404, message="id <{}> doesn't exist".format(id))
class r_product_list(Resource):
    def get(self):
        # Product继承了db.Model的query.all方法，根据Product里面设定好的字段，进行query
        limit = request.args.get('limit')
        if limit:
            all_products = models.Product.query.limit(limit)
        else:
            all_products = models.Product.query.all()
        # one_product = Product.query.get(id) 按照primarykey查询
        result = products_schema.dump(all_products)
        
        return result.data
    def post(self):
        name = request.json['name']
        description = request.json['description']
        price = request.json['price']
        # 初始化产品模型
        new_product = models.Product(name, description, price)
        # 添加以及提交
        db.session.add(new_product)
        db.session.commit()
        # product_schema集成了Schema的方法，返回MarshalResult对象，使用dump使obj->dict
        result = product_schema.dump(new_product)

        # MarshalResult(data={'name': 'Marry', 'price': 45.5, 'description': 'ddd', 'id': 17}, errors={})
        return result.data, 201
class r_product(Resource):
    def put(self, id):
        try_error(id)
        product = models.Product.query.get(id) # 按照primarykey查询
        name = request.json['name']
        description = request.json['description']
        price = request.json['price']

        product.name = name
        product.description = description
        product.price = price
        
        db.session.commit()

        return product_schema.dump(product).data, 201
    def delete(self, id):
        try_error(id)
        product = models.Product.query.get(id)
        db.session.delete(product)
        db.session.commit()
        return '', 204
    def get(self, id):
        try_error(id)
        product = models.Product.query.get(id)
        return product_schema.dump(product).data, 200