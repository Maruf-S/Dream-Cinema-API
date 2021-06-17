import uuid
from uuid import UUID,uuid4
from flask_sqlalchemy import *

from sqlalchemy.dialects.postgresql import UUID

from sqlalchemy import text as sa_text


from Dream_Cinema_API import db

from Dream_Cinema_API import app

app.app_context().push()

class TicketModel(db.Model):
    ticket_id = db.Column('id', db.Text(length=36), default=lambda: str(uuid.uuid4()), primary_key=True) #db.Column(UUID(as_uuid=True), primary_key=True, server_default=sa_text("uuid_generate_v4()"))#db.Column( uuid.UUID, unique=True, nullable=False, default=uuid.uuid4)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'),nullable=False)
    movie_id = db.Column(db.Integer , db.ForeignKey('movies.id'), nullable=False)
    

    # def __repr__(self):
    #     return f"Ticket No.('{self.ticket_no}')"
    
    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()