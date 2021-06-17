
from flask.globals import request
from datetime import datetime
from flask_restplus import Resource,fields
from flask_jwt import jwt_required
from Dream_Cinema_API.models.ticket import TicketModel
from Dream_Cinema_API.ma import *
from Dream_Cinema_API import api


ticket_schema = TicketSchema()
tickets_schema = TicketSchema(many=True)

ticket = api.model("Ticket", {
        'user_id' : fields.Integer,
        'movie_id' : fields.Integer,
        
    })

class TicketList(Resource):
    

    def get(self):
        '''
            Get all Tickets
        '''
        tickets = TicketModel.query.all()
        if tickets:
            return tickets_schema.dump(tickets), 200
        return {"message" : "No tickets"}, 400


    
    @api.expect(ticket)
    def post(self):
        '''
            Create a new ticket

        '''
       
        new_ticket = TicketModel()
        new_ticket.user_id = request.json['user_id']
        new_ticket.movie_id = request.json['movie_id']
        new_ticket.save_to_db()
        
        return {"message": "Ticket added successfully."}, 201

class Ticket(Resource):

    def get(self, id):
        '''
            Get a single ticket

        '''
        ticket = TicketModel.query.filter_by(ticket_id=id).first()

        if ticket:
            return ticket_schema.dump(ticket),200
        return {"message": "Ticket is not found!"}, 404

    # @jwt_required
    def delete(self,id):
        '''
            Delete a ticket from Database
        '''

        ticket = TicketModel.query.filter_by(user_id=id).first()
        if ticket:
            ticket.delete_from_db()
            return {"message": "Ticket is successfully deleted!"}, 200
        return {"message": "Ticket is not found!"}, 404

    # @jwt_required
    # @api.expect(ticket)
    # def put(self, id):
    #     '''
    #         Update an existing ticket
    #     '''

    #     ticketToEdit = TicketModel.query.filter_by(id=id).first()
    #     # try :
    #     if ticketToEdit:

    #         ticketToEdit.ticket_no = request.json['ticket_no']
            
    #         ticketToEdit.save_to_db()
    #         return ticket_schema.dump(ticketToEdit), 200
        
    #     return {"message" : "Ticket not found"}, 404
        # except:
        #     return {"message" : "Please Try Again"}