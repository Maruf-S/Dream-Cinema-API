from datetime import datetime
from typing import Text
from flask_restplus import Resource, reqparse, fields
from flask import jsonify, request
from flask_jwt import *

from Dream_Cinema_API.models.movie import MovieModel
from Dream_Cinema_API.ma import *
from Dream_Cinema_API import api

movie_schema = MovieSchema()
movies_schema = MovieSchema(many=True)

class MovieList(Resource):
    
    movie = api.model("Movie", {
        'Title': fields.String('Name of the Movie'),
        'Description': fields.String,
        'Postor' : fields.String('Poster url'),
        'Background': fields.String('Background url'),
        'Trailer': fields.String('trailer url'),
        'Screening': fields.DateTime,
        'Genre': fields.String,
        'IDMBRating': fields.Float,
        'AiredBy': fields.String,
        'ReleaseDate': fields.DateTime,
        'Ticket' : fields.String
    })

    def get(self):
        ''' 
            Get All Movies from the Database
        '''
        movies = MovieModel.query.all()
        if movies:
            return movies_schema.dump(movies), 200
        return {"message" : "No movies in the Database"}, 404

    @api.expect(movie)
    def post(self):
        '''
            Create a new movie
        '''
        new_movie = MovieModel()
        scdate = request.json['Screening']
        reldate = request.json['ReleaseDate']
        new_movie.Title = request.json['Title']
        new_movie.Description = request.json['Description']
        new_movie.Postor = request.json['Postor']
        new_movie.Background = request.json['Background']
        new_movie.Trailer = request.json['Trailer']
        new_movie.Screening = datetime(int(scdate[6:10]), int(scdate[:2]), int(scdate[3:5]),int(scdate[11:13]), int(scdate[14:16]), 00)
        new_movie.Genre = request.json['Genre']
        new_movie.IDMBRating = request.json['IDMBRating']
        new_movie.AiredBy = request.json['AiredBy']
        new_movie.ReleaseDate = datetime(int(reldate[6:10]), int(reldate[:2]), int(reldate[3:5]), 00, 00, 00)
        new_movie.Ticket = request.json['Ticket']

        new_movie.save_to_db()
        return movie_schema.dump(new_movie), 201
        
class Movie(Resource):

    movie = api.model("Movie", {
        'Title': fields.String('Name of the Movie'),
        'Description': fields.String,
        'Postor' : fields.String('Poster url'),
        'Background': fields.String('Background url'),
        'Trailer': fields.String('trailer url'),
        'Screening': fields.DateTime,
        'Genre': fields.String,
        'IDMBRating': fields.Float,
        'AiredBy': fields.String,
        'ReleaseDate': fields.DateTime,
        'Ticket' : fields.String
    })

    def get(self, id):
        '''
            Get a movie by id
        '''
        movie = MovieModel.find_by_id(id)
        if movie:
            return movie_schema.dump(movie),200
        return {"message": "Movie is not found!"}, 404

    @api.expect(movie)
    def put(self, id):
        '''
            Update an existing movie
        '''

        movieToEdit = MovieModel().query.filter_by(id=id).first()

        if movieToEdit:
            scdate = request.json['Screening']
            reldate = request.json['ReleaseDate']

            movieToEdit.Title = request.json['Title']
            movieToEdit.Description = request.json['Description']
            movieToEdit.Postor = request.json['Postor']
            movieToEdit.Background = request.json['Background']
            movieToEdit.Trailer = request.json['Trailer']
            movieToEdit.Screening = datetime(int(scdate[6:10]), int(scdate[:2]), int(scdate[3:5]),int(scdate[11:13]), int(scdate[14:16]), 00)
            movieToEdit.Genre = request.json['Genre']
            movieToEdit.IDMBRating = request.json['IDMBRating']
            movieToEdit.AiredBy = request.json['AiredBy']
            movieToEdit.ReleaseDate = datetime(int(reldate[6:10]), int(reldate[:2]), int(reldate[3:5]))
            movieToEdit.Ticket = request.json['Ticket']

            movieToEdit.save_to_db()
            return movie_schema.dump(movieToEdit), 200
        
        return {"message" : "Movie not found"}, 404
<<<<<<< Updated upstream
<<<<<<< Updated upstream

=======
>>>>>>> Stashed changes
=======
>>>>>>> Stashed changes

    def delete(self, id):
        '''
            Delete a movie from Database
        '''
        movie = MovieModel.find_by_id(id)
        if movie:
            movie.delete_from_db()
            return {"message": "Movie is successfully deleted!"}, 200
        return {"message": "Movie is not found!"}, 404

    















