
from entities.user import User
import re, sys , pdb

class UserInputError(Exception):
    pass


class AuthenticationError(Exception):
    pass


class UserService:
    def __init__(self, user_repository):
        self._user_repository = user_repository

    def check_credentials(self, username, password):


        if not username or not password:
            raise UserInputError("Username and password are required")

        user = self._user_repository.find_by_username(username)

        if not user or user.password != password:
            raise AuthenticationError("Invalid username or password")

        return user

    def create_user(self, username, password):
        self.validate(username, password)

        user = self._user_repository.create(
            User(username, password)
        )

        return user

    def validate(self, username, password):
        if not username or not password:
            raise UserInputError("Username and password are required")

        if self._user_repository.find_by_username(username):
            raise UserInputError("Username is already in use")
        
        if bool(re.match("^[a-z]+$", username) == False) or (len(username) < 3):
            raise UserInputError("Username must contain at least 3 characters from [a-z]")
        
        if (re.match("^[a-z]+$", password)) or (len(password) < 8):
            raise UserInputError("Password should contain at least one number and min lenght is 8")

        # toteuta loput tarkastukset tänne ja nosta virhe virhetilanteissa