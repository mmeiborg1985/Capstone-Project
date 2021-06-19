from flask import Flask, render_template,request, redirect, jsonify, session
from models import db, connect_db, Players, User, roster
from flask_sqlalchemy import SQLAlchemy
from forms import RegisterForm, LoginForm, DeleteForm
from flask_bcrypt import Bcrypt






app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']= 'postgresql:///capstone_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']= False
app.config['SQLALCHEMY_ECHO']= True
app.config['SECRET_KEY'] = "shhhhh"

connect_db(app)


##register and login/logout

@app.route("/")
def homepage():
    """Homepage of site; redirect to register."""

    return redirect("/register")


@app.route('/register', methods=['GET', 'POST'])
def register():
    """Register a user: produce form and handle form submission."""

    if "username" in session:
        return redirect(f"/login")

    form = RegisterForm()

    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        first_name = form.first_name.data
        last_name = form.last_name.data
        email = form.email.data

        user = User.register(username, password, first_name, last_name, email)

        db.session.commit()
        session['username'] = user.username

        return redirect(f"/users/{user.username}")

    else:
        return render_template("register.html", form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    """Produce login form or handle login."""

    if "username" in session:
        return redirect(f"/list")

    form = LoginForm()

    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data

        user = User.authenticate(username, password)  # <User> or False
        if user:
            session['username'] = user.username
            return redirect(f"/list")
        else:
            form.username.errors = ["Invalid username/password."]
            return render_template("login.html", form=form)

    return render_template("login.html", form=form)


@app.route("/logout")
def logout():
    """Logout route."""

    session.pop("username")
    return redirect("/login")










##player routes
@app.route("/list")
def show_all_players():
    """Return a list of players."""
    players = Players.query.all()
    return render_template("home.html", players=players)

@app.route("/<int:player_id>")
def show_player(player_id):
    """Show info on a single player."""

    player = Players.query.get_or_404(player_id)
    return render_template("player.html", player=player)

@app.route("/list", methods=["POST"])
def add_player():
    """Add player and redirect to list."""

    player_id = request.form['player_id']
    name = request.form['name']
    position = request.form['position']
    team = request.form['team']
    adp = request.form['adp']
    high = request.form['high']
    low = request.form['low']
    stdev = request.form['stdev']
    bye = request.form['bye']

    

    player = Players(player_id=player_id, name=name, position=position, team=team, adp=adp, high=high, low=low, stdev=stdev, bye=bye)
    db.session.add(player)
    db.session.commit()

    return redirect(f"/list")

##update player
@app.route('/<int:player_id>', methods=["PATCH"])
def update_player(player_id):
    player=players.query.get_or_404(player_id)
    player.player_id = request.json.get('player_id', player.player_id)
    player.name = request.json.get('name', player.name)
    player.team = request.json.get('team', player.team)
    player.adp = request.json.get('adp', player.adp)
    player.high = request.json.get('high', player.high)
    player.low = request.json.get('low', player.low)
    player.stdev = request.json.get('stdev', player.stdev)
    player.bye = request.json.get('bye', player.bye)
    
    db.session.commit()
    return jsonify(player=player.serialize())

##delete player
@app.route('/<int:player_id>', methods=['DELETE'])
def delete_player(player_id):
    player = Players.query.get_or_404(player_id)
    db.session.delete(player)
    db.session.commit()
    return jsonify(message="deleted")

##roster routes
@app.route('/roster')   
def show_team():
    """Return a list of roster."""
    team = roster.query.all()
    return render_template("roster.html", team=team) 

@app.route("/roster", methods=["POST"])
def add_roster():
    """Add player and redirect to list."""

    player_name = request.form['player_name']
    player_position = request.form['player_position']
    team = roster(player_name=player_name, player_position=player_position)
    db.session.add(team)
    db.session.commit()

    return redirect(f"/roster")














if __name__ == '__main__':
   app.run()

