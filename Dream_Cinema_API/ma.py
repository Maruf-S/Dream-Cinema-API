from flask_marshmallow import Marshmallow
from Dream_Cinema_API.models.user import *
from Dream_Cinema_API.models.movie import *
from Dream_Cinema_API.models.comment import *
from Dream_Cinema_API.models.movieComment import *
from Dream_Cinema_API.models.ticket import *
ma = Marshmallow()


class MovieSchema(ma.Schema):
    class Meta:
        fields = ('id',"Title", "Description","Postor", "Background","Trailer","Screening","Genre","IDMBRating", "AiredBy",
                  "ReleaseDate","Ticket")

        model = MovieModel


class UserSchema(ma.Schema):
    class Meta:
        fields = ('id',"Username", "Email", "Password","Admin","Image","Twitter_link","Instagram_link")

        model = UserModel

class CommentSchema(ma.Schema):
    class Meta:
        fields = ("user_id", "movie_id", "comment","rating","date")

        model = CommentModel


class MovieCommentSchema(ma.Schema):
    class Meta:
        fields = ("Email", "Comment", "Date")

        model = MovieCommentModel


class MovieCommentSchema(ma.Schema):
    class Meta:
        fields = ("Email", "Comment", "Date")

        model = MovieCommentModel       

class TicketSchema(ma.Schema):
    class Meta:
        fields = ("user_id", "movie_id","ticket_id")

        model = TicketModel
        include_fk=True