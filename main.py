# only one resource ie study resource

from flask import Flask
from application.models import Role, User, db
from config import DevelopmentConfig
from application.resources import api
from flask_security import SQLAlchemyUserDatastore,Security




def create_app():
    app=Flask(__name__) 
    # creating instance 

    # loading the configuration 
    app.config.from_object(DevelopmentConfig)


    db.init_app(app)
    api.init_app(app)
    datastore=SQLAlchemyUserDatastore(db,User,Role)
    app.security=Security(app,datastore)
    
    with app.app_context():
        import application.views
        # opening views here
    return app,datastore


app,datastore=create_app()

if __name__=='__main__':
    app.run(debug=True)