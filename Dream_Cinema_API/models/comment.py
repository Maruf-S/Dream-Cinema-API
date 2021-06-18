from Dream_Cinema_API import db
from datetime import datetime

from Dream_Cinema_API import app

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

