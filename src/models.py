from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from datetime import datetime
from . import settings
# init db
db = SQLAlchemy()
# 创建db：本地运行交互环境，from app import db ; db.create_all()会生成sqllite文件
#init ma
ma = Marshmallow()
#Product Class/model 定义好数据模型

class Product(db.Model):
    # 此处建表、以及产品创建用
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

# user段

class User(db.Model):
    user_id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(50), unique=True)
    user_pass = db.Column(db.String(50), nullable=False)
    create_date = db.Column(db.DateTime, default=datetime.now())
    open_id = db.Column(db.String(32), nullable=True)
    def __init__(self, user_name, user_pass, open_id):
        self.user_name = user_name
        self.user_pass = user_pass
        self.open_id = open_id
class UserSchema(ma.Schema):
    class Meta:
        fields = ('user_id', 'user_name', 'user_pass', 'create_date', 'open_id')

class Question(db.Model):
    question_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(256))
    option_a = db.Column(db.String(128))
    option_b = db.Column(db.String(128))
    option_c = db.Column(db.String(128))
    option_d = db.Column(db.String(128))
    answer = db.Column(db.String(4))
    # 这句自动生成当前时间
    create_date = db.Column(db.DateTime, default=datetime.now())
    def __init__(self, title, options, answer):
        self.title = title
        self.option_a = options[0]
        self.option_b = options[1]
        self.option_c = options[2]
        self.option_d = options[3]
        self.answer = answer
class QuestionSchema(ma.Schema):
    class Meta:
        fields = ('title', 'option_a', 'option_b', 'option_c','option_d', 'answer')
def init_app(app):
    db.init_app(app)
    # 数据库设置好之后初始化
    settings.init_config(app)
    # 建表
    # db.create_all(app=app)
    return db