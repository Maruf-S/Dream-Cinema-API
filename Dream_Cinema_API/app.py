from Dream_Cinema_API import app
from flask_restplus import Api, Resource, fields
from Dream_Cinema_API import api
from flask_jwt import JWT, jwt_required, current_identity

from Dream_Cinema_API.resources.user import *
from Dream_Cinema_API.resources.movie import *
from Dream_Cinema_API.resources.comment import *
from Dream_Cinema_API.resources.ticket import *

from Dream_Cinema_API.security import authenticate, identity
from Dream_Cinema_API.models.user import *



@app.before_first_request
def create_tables():
    db.create_all()



jwt = JWT(app, authenticate, identity)

api.add_resource(UserComment, '/api/v1/comment/<int:id>')
api.add_resource(UsersComment, '/api/v1/comment/')
api.add_resource(UsersRegister, '/api/v1/register')
api.add_resource(UserRegister, '/api/v1/register/<int:id>')
api.add_resource(MovieList, '/api/v1/movies')
api.add_resource(Movie, '/api/v1/movie/<int:id>')
api.add_resource(TicketList, '/api/v1/ticket/')
api.add_resource(Ticket, '/api/v1/ticket/<id>')

api.add_resource(CurrentUser, '/api/v1/current_user')

if __name__ == '__main__':
    app.run(port=5000, debug=True)