import sqlalchemy
from flask import Flask, redirect, url_for, render_template, flash
from flask_login import LoginManager, UserMixin, login_user, logout_user,\
    current_user
from Login.oauth import OAuthSignIn

from sqlalchemy import create_engine, Boolean, Column, DateTime, ForeignKey, Integer, Numeric, Text, text, Time, CheckConstraint
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base


app = Flask(__name__)
app.config['SECRET_KEY'] = 'top secret!'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
app.config['OAUTH_CREDENTIALS'] = {
    'facebook': {
        'id': '855582984606741',
        'secret': 'ea299d150dfc97eb98eabc4e4b5c1e8c'
    },
    'twitter': {
        'id': '3RzWQclolxWZIMq5LJqzRZPTl',
        'secret': 'm9TEd58DSEtRrZHpz2EjrV9AhsBRxKMo8m3kuIZj3zLwzwIimt'
    }
}


engine = create_engine('postgresql://cmesser:Bedlum!1@localhost/postgres')
db_session = sessionmaker(bind=engine)

db = db_session
lm = LoginManager(app)
lm.login_view = 'index'


Base = declarative_base()
metadata = Base.metadata


class User(Base):
    __tablename__ = 'users'
    __table_args__ = (
        CheckConstraint("date_part('timezone'::text, created_at) = '0'::double precision"),
        CheckConstraint("date_part('timezone'::text, updated_at) = '0'::double precision")
    )

    id = Column(Integer, primary_key=True, server_default=text("nextval('users_id_seq'::regclass)"))
    social = Column(Text)
    nickname = Column(Text)
    email = Column(Text)
    updated_at = Column(DateTime(True), nullable=False, server_default=text("now_utc()"))
    created_at = Column(DateTime(True), nullable=False, server_default=text("now_utc()"))


# class User(UserMixin, db.Model):
#     __tablename__ = 'users'
#     id = db.Column(db.Integer, primary_key=True)
#     social_id = db.Column(db.String(64), nullable=False, unique=True)
#     nickname = db.Column(db.String(64), nullable=False)
#     email = db.Column(db.String(64), nullable=True)


@lm.user_loader
def load_user(id):
    return User.query.get(int(id))


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))


@app.route('/authorize/<provider>')
def oauth_authorize(provider):
    if not current_user.is_anonymous:
        return redirect(url_for('index'))
    oauth = OAuthSignIn.get_provider(provider)
    return oauth.authorize()


@app.route('/callback/<provider>')
def oauth_callback(provider):
    if not current_user.is_anonymous:
        return redirect(url_for('index'))
    oauth = OAuthSignIn.get_provider(provider)
    social_id, username, email = oauth.callback()
    if social_id is None:
        flash('Authentication failed.')
        return redirect(url_for('index'))
    user = User.query.filter_by(social_id=social_id).first()
    if not user:
        user = User(social_id=social_id, nickname=username, email=email)
        db.add(user)
        db.commit()
    login_user(user, True)
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)
