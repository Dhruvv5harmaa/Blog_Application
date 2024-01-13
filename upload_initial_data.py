from main import app
from application.models import db,Role


with app.app_context():
    db.create_all() 
    datastore.find_or_create_role(name="admin",desciption="User is an admin")
    db.session.commit()
    if not datastore.find_user(email="admin@email.com"):
        datastore.create_user(email="admin@email.com",password="admin",roles=["admin"])

    if not datastore.find_user    


    # admin=Role(id='admin',name='Admin',description='Admin description')
    # db.session.add(admin)
    # stud=Role(id='stud',name='Student',description='Student description')
    # db.session.add(stud)
    # inst=Role(id='inst',name='Instructor',description='Instructor description')
    # db.session.add(inst)


    # this above thing is to make table entry at first time 
    # but when next time we have to open this this might throw error 
    # that is why we are using try catch.


    try:
        db.session.commit()

    except:
        pass    
       
    # this will create all table