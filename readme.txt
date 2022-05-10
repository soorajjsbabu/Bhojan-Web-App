pipenv shell

export FLASK_APP=api
export FLASK_DEBUG=1
flask run

kill port:
sudo fuser -k 5000/tcp 

db creation(python3):
from backend.models import Donation, User
from backend import db, create_app
db.create_all(app=create_app())

db access(sqlite3):
.open backend/database.db
