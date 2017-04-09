from werkzeug.security import safe_str_cmp
from models.user import UserModel
from oauth2client import client, crypt

def authenticate(username, password):
    """
    Verify user for JWT to return token on /auth endpoint.
    """
    user = UserModel.find_by_username(username)
    # Check whether the user logged in with oauth.
    if user.oauth:
        client_id = '468635640034-rp3e0rdggu885nbvtjvtis70u7g7vt1h.apps.googleusercontent.com'
        idinfo = client.verify_id_token(password, client_id)
        # Check if the token is correct
        if idinfo['iss'] not in ['accounts.google.com', 'https://accounts.google.com']:
            raise crypt.AppIdentityError("Wrong issuer.")
        return user
    # Otherwise use the password to verify the user
    else:
        if user and safe_str_cmp(user.password, password):
            return user

def identity(payload):
    """
    Verify identity of user
    """
    user_id = payload['identity']
    return UserModel.find_by_id(user_id)
