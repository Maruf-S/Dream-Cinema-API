from datetime import datetime
from typing import Text
from flask_restplus import Resource, reqparse, fields
from flask import jsonify, request
from flask_jwt import *

from Dream_Cinema_API.models.movie import MovieModel
from Dream_Cinema_API.ma import *
from Dream_Cinema_API import api
import dateutil.parser
from werkzeug.utils import secure_filename
import os
import json

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

    # @api.expect(movie)
    def post(self):
        '''
            Create a new movie
        '''
<<<<<<< HEAD
        print("---------_________----0")
        BudgetJson = json.loads(request.form['json'])
        print(BudgetJson)
        file = request.files
        print(file)
        imgBg = file['ImgBig']
        imgSm = file['ImgSml']
        imgBgName = secure_filename(imgBg.filename)
        imgSmName = secure_filename(imgSm.filename)
        imgBg.save(os.path.join(app.root_path, 'ImageUploads',imgBgName ))
        imgSm.save(os.path.join(app.root_path, 'ImageUploads', imgSmName))
=======

        
>>>>>>> 229ecf3f8f03bbeacb40e725d66e837ca13abc03
        new_movie = MovieModel()
        scdate = BudgetJson.get('Screening')
        reldate = BudgetJson.get('ReleaseDate')
        new_movie.Title = BudgetJson.get('Title')
        new_movie.Description = BudgetJson.get('Description')
        new_movie.Postor = imgSmName
        new_movie.Background = imgBgName
        new_movie.Trailer = BudgetJson.get('Trailer')
        new_movie.Screening = dateutil.parser.isoparse(scdate)
        new_movie.Genre = BudgetJson.get('Genre')
        new_movie.IDMBRating = BudgetJson.get('IDMBRating')
        new_movie.AiredBy = BudgetJson.get('AiredBy')
        new_movie.ReleaseDate = dateutil.parser.isoparse(reldate)
        new_movie.Ticket = BudgetJson.get('Ticket')
        print(new_movie.ReleaseDate)
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
            movieToEdit.Screening = dateutil.parser.isoparse(scdate)
            movieToEdit.Genre = request.json['Genre']
            movieToEdit.IDMBRating = request.json['IDMBRating']
            movieToEdit.AiredBy = request.json['AiredBy']
            movieToEdit.ReleaseDate = dateutil.parser.isoparse(reldate)
            movieToEdit.Ticket = request.json['Ticket']

            movieToEdit.save_to_db()
            return movie_schema.dump(movieToEdit), 200
        
        return {"message" : "Movie not found"}, 404

    def delete(self, id):
        '''
            Delete a movie from Database
        '''
        movie = MovieModel.find_by_id(id)
        if movie:
            movie.delete_from_db()
            return {"message": "Movie is successfully deleted!"}, 200
        return {"message": "Movie is not found!"}, 404

    















