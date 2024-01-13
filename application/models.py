from flask_sqlalchemy import SQLAlchemy
from flask_security import UserMixin,RoleMixin
db=SQLAlchemy()
# db is a sqlalchemy instance



class RoleUsers(db.Model): 
    __tablename__='roles_users'
    id = db.Column(db.Integer, primary_key=True)
    user_id=db.Column(db.Integer ,db.ForeignKey('user.id'))
    role_id=db.Column(db.Integer ,db.ForeignKey('role.id'))
    
    


class User(db.Model,UserMixin):
    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    username = db.Column(db.String, unique=False)
    email = db.Column(db.String, unique=True)
    password = db.Column(db.String(255))
    active = db.Column(db.Boolean())
    fs_uniquifier = db.Column(db.String(255), unique=True, nullable=False)

    # relationship from different table
    # role_id=db.Column(db.String ,db.ForeignKey('role.id'))
    # role=db.relationship('Role')
    roles = db.relationship('Role', secondary='roles_users',
                         backref=db.backref('users', lazy='dynamic'))
    # study_resource = db.relationship('StudyResource', backref='creator')


class Role(db.Model,RoleMixin):
    id = db.Column(db.Integer(), primary_key=True)
    # fixed roles student instructor 
    name = db.Column(db.String(80), unique=True)
    description = db.Column(db.String(255))

class StudyResource(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    topic=db.Column(db.String(),nullable=False)
    resource_link=db.Column(db.String, unique=True)
    description=db.Column(db.String,nullable=False)
    is_approved=db.Column(db.Boolean(),default=False)

    # creator_id=db.Column(db.Integer,db.ForeignKey('user.id'),nullable=False)
