from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt


bcrypt = Bcrypt()
db= SQLAlchemy()

def connect_db(app):
    db.app=app
    db.init_app(app)

class Players(db.Model):

    __tablename__= "players"

    player_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(10000))
    position = db.Column(db.String(2))
    team= db.Column(db.String(100))
    adp = db.Column(db.Float)
    high = db.Column(db.Integer)
    low = db.Column(db.Integer)
    stdev = db.Column(db.Integer)
    bye = db.Column(db.Integer)

    def serialize(self):
        return{
            "player_id": players.player_id,
            "name": players.name,
            "postion": players.position,
            "team":  players.team,
            "adp":  players.adp,
            "high": players.high,
            "low":  players.low,
            "stdev": players.stdev,
            "bye":  players.bye,
        }

    def __repr__(self):
        """Show info about player."""

        p = self
        return f"{p.player_id} {p.name} {p.position} {p.team} {p.adp} {p.high} {p.low} {p.stdev} {p.bye}"  
        
class roster(db.Model):

    __tablename__= "roster"

    player_name = db.Column(db.String(10000), primary_key=True)
    player_position = db.Column(db.String(2))

    def __repr__(self):

        pl= self
        return f"{pl.player_name} {pl.player_position}"


class User(db.Model):
    

    __tablename__ = "users"

    username = db.Column(
        db.String(20),
        nullable=False,
        unique=True,
        primary_key=True,
    )
    password = db.Column(db.Text, nullable=False)
    email = db.Column(db.String(50), nullable=False)
    first_name = db.Column(db.String(30), nullable=False)
    last_name = db.Column(db.String(30), nullable=False)

    

    # start of convenience class methods

    @classmethod
    def register(cls, username, password, first_name, last_name, email):
        """Register a user, hashing their password."""

        hashed = bcrypt.generate_password_hash(password)
        hashed_utf8 = hashed.decode("utf8")
        user = cls(
            username=username,
            password=hashed_utf8,
            first_name=first_name,
            last_name=last_name,
            email=email
        )

        db.session.add(user)
        return user

    @classmethod
    def authenticate(cls, username, password):
        """Validate that user exists & password is correct.

        Return user if valid; else return False.
        """

        user = User.query.filter_by(username=username).first()

        if user and bcrypt.check_password_hash(user.password, password):
            return user
        else:
            return False
