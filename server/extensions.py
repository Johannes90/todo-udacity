from flask_restful import Api
from flask_jwt import JWT
from flask_cors import CORS
from flask_bcrypt import Bcrypt
from flask_migrate import Migrate

# Adding the extensions
migrate = Migrate()
cors = CORS()
api = Api()
bcrypt = Bcrypt()
jwt = JWT()
