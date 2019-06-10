from flask import Flask
from flask_restful import Api
from src import models, view

# 初始化app
app = Flask(__name__)
# restful绑定
api = Api(app)
# 将数据库模型与app绑定
db = models.init_app(app)

api.add_resource(view.r_product_list, '/product')
api.add_resource(view.r_product, '/product/<id>')

api.add_resource(view.r_user_list, '/user')
if __name__ == '__main__':
    app.run(debug=True, port=5000)