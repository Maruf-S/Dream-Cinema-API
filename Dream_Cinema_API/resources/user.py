from flask import request,jsonify
from flask_restplus import Resource, reqparse, Api, fields
from flask_jwt import current_identity
from flask_jwt import jwt_required

from Dream_Cinema_API.models.user import *
from Dream_Cinema_API.ma import *
from Dream_Cinema_API import api
from Dream_Cinema_API import bcrypt


user_schema = UserSchema()
users_schema = UserSchema(many=True)


# Model required by flask_restplus for expect
user = api.model("User", {
    'Email': fields.String('User Email'),
    'Password': fields.String
    
})
class UsersRegister(Resource):
    # @jwt_required
    def get(self):
        ''' 
            Get All Users from the Database
        '''
        users = UserModel.query.all()
        return users_schema.dump(users),200 if users else 404
    

    @api.expect(user)
    def post(self):
        '''
            Create a new User
        '''
        Username = request.json['Email']
        Email = request.json['Email']
        Password = request.json['Password']
        hashedPS = bcrypt.generate_password_hash(Password).decode('utf-8')

        if UserModel.find_by_email(Email):
            return {"message": "Email is already taken"}, 409
        
        new_user = UserModel()
        new_user.Username = Email
        new_user.Email = Email
        new_user.Password = hashedPS
        new_user.save_to_db()
        return user_schema.dump(new_user), 201


    @jwt_required()
    @api.expect(user)
    def put(self):
        '''
            Update an existing User
        '''
        
        user = current_identity
        if user:
            data = request.get_json()
            j = []
            for i in data:
                j.append(i)
            if "Instagram_link" in j and "Twitter_link" in j:
                user.Instagram_link = data['Instagram_link']
                user.Twitter_link = data['Twitter_link']
            elif "Password" in j:
                hashedPS = bcrypt.generate_password_hash(data['Password']).decode('utf-8')
                user.Password = hashedPS
            elif "Email" in j:
                user.Email = data['Email']
            else:
                return {"message": "Nothing to update"}, 
            user.save_to_db()
            return user_schema.dump(user), 200

        return {"message": "User is not found!"}, 404

        
    @jwt_required()
    def delete(self):
        '''
            delete a user from database
        '''
        # return user_schema.dump(current_identity)
        user = current_identity
        if user:
            user.delete_from_db()
            return {"message": "User is successfully deleted!"}, 200
        return {"message": "User is not found!"}, 404
        

class UserRegister(Resource):
    
    def get(self, id):
        '''
            Get a User by id
        '''
        user = UserModel.find_by_id(id)
        if user:
            return user_schema.dump(user),200
        return {"message": "User is not found!"}, 404


class CurrentUser(Resource):
    @jwt_required()
    def get(self):
        '''
            get current user
        '''
        return user_schema.dump(current_identity)
