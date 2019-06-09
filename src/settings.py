import os
basedir = os.path.abspath(os.path.dirname(__file__))
def init_config(app):
  app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+ os.path.join(basedir, 'database', 'db.sqlite')
  app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False