from Dream_Cinema_API import db
from datetime import datetime
from Dream_Cinema_API import app
from Dream_Cinema_API.models.user import UserModel
from Dream_Cinema_API.models.movie import MovieModel
from Dream_Cinema_API.models.movieComment import MovieCommentModel
app.app_context().push()

class CommentModel(db.Model):
    id = db.Column(db.Integer ,primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'),nullable=False)
    movie_id = db.Column(db.Integer , db.ForeignKey('movies.id'), nullable=False)
    comment = db.Column(db.String(), nullable=False)
    date = db.Column(db.DateTime, default=datetime.utcnow)

    # def __init__(self, user_id, movie_id, comment, rating, date):
    #     self.user_id = user_id
    #     self.comment = comment
    #     self.movie_id = movie_id
    #     self.comment = comment
    #     self.date = date

    # def __repr__(self):
    #     return f"Comment('{self.comment}')"

    


    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
    
    @classmethod
    def getAll(cls,mov_id):
        result = db.session.query().join(UserModel,UserModel.id == CommentModel.user_id).join(MovieModel, MovieModel.id==mov_id).add_columns( MovieModel.Title, CommentModel.comment, CommentModel.date,UserModel.Email).all()
        if(not result):
            return result
        mappedRes = []
        for item in result:
            mappedRes.append(MovieCommentModel(Comment=item['comment'],Email=item['Email'],Date=item['date']))
        return mappedRes


#     @classmethod
#     def find_by_id(cls, _id):
#         return cls.query.filter_by(id=_id).first()


#     def jsonify(self):
#         return {
#             "comment" : self.comment,
#             "rating" : self.rating,
#             "movie_id" : self.movie_id
#             "user_id" : self.user_id
#             "date" : self.date
#         }
print((CommentModel.getAll(1)))
