from flask.globals import request
from datetime import datetime
from flask_restplus import Resource,fields
from flask_jwt import jwt_required
from Dream_Cinema_API.models.comment import CommentModel
from Dream_Cinema_API.ma import *
from Dream_Cinema_API import api
from flask import jsonify
import datetime

comment_schema = CommentSchema()
comments_schema = CommentSchema(many=True)
movie_comment_schema = MovieCommentSchema(many=True)

class UsersComment(Resource):
    comment = api.model("Comment", {
        'user_id' : fields.Integer,
        'movie_id' : fields.Integer,
        'comment' : fields.String('The Comment'),
        'date' : fields.DateTime
    })


    def get(self):
        '''
            Get all comments

        '''
        comments = CommentModel.all()
        if comments:
            return comments_schema.dump(comments), 200
        return {"message" : "No comments"}, 400


    
    @api.expect(comment)
    def post(self):
        '''
            Create a new comment

        '''
       
        new_comment = CommentModel()
        datejson = request.json['date']
        new_comment.user_id = request.json['user_id']
        new_comment.movie_id = request.json['movie_id']
        new_comment.comment = request.json['comment']
        new_comment.date = datetime.datetime.now()
        new_comment.save_to_db()
        
        return {"message": "Comment added successfully."}, 201

class UserComment(Resource):
    comment = api.model("Comment", {
        'user_id' : fields.Integer,
        'movie_id' : fields.Integer,
        'comment' : fields.String('The Comment'),
        'rating' : fields.Float,
        'date' : fields.DateTime
    })

    commentn = api.model("MovieComment", {
        'Email' : fields.String,
        'Comment' : fields.String('The Comment'),
        'Date' : fields.DateTime
    })

    def get(self, id):
        '''
            Get comments for a certian movie

        '''
        commentn = CommentModel.getAll(mov_id=id);
        print(commentn)

        # comment = CommentModel.query.filter_by(id=id).first()

        if commentn:
            return movie_comment_schema.dump(commentn),200
        return {"message": "No comments exist for this movie"}, 404

    def delete(self, id):
        '''
            Delete a comment from Database
        '''
        comment = CommentModel.query.filter_by(id=id).first()
        if comment:
            comment.delete_from_db()
            return {"message": "Comment is successfully deleted!"}, 200
        return {"message": "Comment is not found!"}, 404

    @api.expect(comment)
    def put(self, id):
        '''
            Update an existing comment
        '''

        commentToEdit = CommentModel.query.filter_by(id=id).first()
        # try :
        if commentToEdit:
            datejson = request.json['date']

            commentToEdit.comment = request.json['comment']
            commentToEdit.date = datetime(int(datejson[:4]), int(datejson[5:7]), int(datejson[8:10]),int(datejson[11:13]), int(datejson[14:16]), int(datejson[17:19]))
            
            commentToEdit.save_to_db()
            return comment_schema.dump(commentToEdit), 200
        
        return {"message" : "Comment not found"}, 404
        # except:
        #     return {"message" : "Please Try Again"}