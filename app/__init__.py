from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask import Flask
from flask_wtf.csrf import CSRFProtect


app = Flask(__name__)

app.config['SECRET_KEY'] = 'v\xf9\xf7\x11\x13\x18\xfaMYp\xed_\xe8\xc9w\x06\x8e\xf0f\xd2\xba\xfd\x8c\xda'
app.config['SQLALCHEMY_DATABASE_URI'] = ''
# added just to suppress a warning
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

csrf = CSRFProtect(app)

db = SQLAlchemy(app)
UPLOAD_FOLDER = './app/static/uploads'

# Flask_Login login manager
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

app.config.from_object(__name__)