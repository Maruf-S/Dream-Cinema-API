from Dream_Cinema_API import db

from Dream_Cinema_API import app

app.app_context().push()

class TicketModel(db.Model):
    id = db.Column(db.Integer ,primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'),nullable=False)
    movie_id = db.Column(db.Integer , db.ForeignKey('movies.id'), nullable=False)
    ticket_no = db.Column(db.Integer, unique=True, nullable=False)

    def __repr__(self):
        return f"Ticket No.('{self.ticket_no}')"

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()