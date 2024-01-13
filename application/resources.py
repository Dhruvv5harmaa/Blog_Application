# creating flask restful instance here
from flask_restful import Resource, Api ,reqparse,marshal_with,fields
from .models import StudyResource,db

api=Api(prefix='/api')

parser=reqparse.RequestParser()
parser.add_argument('topic',type=str,help='Topic should be a String',required=True)
parser.add_argument('description',type=str,help='Description should be a String',required=True)
parser.add_argument('resource_link',type=str,help='Resource Link should be a String',required=True)
# when client sending some request object it will parse the object and 
# convert it into a nice python dictionary


study_material_fields={
    'id':fields.Integer,
    'topic':fields.String,
    'description':fields.String,
    'resource_link':fields.String
}

class StudyMaterial(Resource):
    @marshal_with(study_material_fields)
    def get(self):
        all_study_material=StudyResource.query.all()  #queriying all the table
        if len(all_study_material)>0: return {"message":"No resource found"},404  #404 is status code of the response
        
        return all_study_material # returning a JSON Object

    def post(self):
        args=parser.parse_args()
        study_resource=StudyResource(**args)
        db.session.add(study_resource)
        db.session.commit()
        return{"message":"Study Resource Created"}

api.add_resource(StudyMaterial,'/study_material')
