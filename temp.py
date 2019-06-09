from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
import flask_restful as restful
# 初始化
app = Flask(__name__)
api = restful.Api(app)
# 200成功，201添加，204修改，404失败
# get 200, post-put 201, del 204, fail 404
def try_error(name):
    if name not in comments.keys():
        restful.abort(404, message="name <{}> doesn't exist".format(name))
class MongoApi(restful.Resource):
	def put(self):
		# 返回的第二个参数是status_code
		return request.json
	def post(self):
		return request.json
api.add_resource(MongoApi,'/comments')

if __name__ == '__main__':
	app.run(host='0.0.0.0', debug=True)
