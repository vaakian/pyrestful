from flask import Flask
from flask_restful import Api
from src import models, view, settings

# 初始化app
app = Flask(__name__)
# restful绑定
api = Api(app)
# 数据库设置好之后初始化
settings.init_config(app)
# 将数据库模型与app绑定
models.init_app(app)

api.add_resource(view.r_product_list, '/product')
api.add_resource(view.r_product, '/product/<id>')
if __name__ == '__main__':
    app.run(debug=True, port=5000)