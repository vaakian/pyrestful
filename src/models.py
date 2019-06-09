from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

# init db
db = SQLAlchemy()
# 创建db：本地运行交互环境，from app import db ; db.create_all()会生成sqllite文件
#init ma
ma = Marshmallow()
#Product Class/model 定义好数据模型
def init_app(app):
    db.init_app(app)
    
class Product(db.Model):
    # 此处建表用
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True)
    description = db.Column(db.String(200))
    price = db.Column(db.Float)
    def __init__(self, name, description, price):
        self.name = name
        self.description = description
        self.price = price
# ProductSchema 定义好数据字段
class ProductSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'description', 'price')



