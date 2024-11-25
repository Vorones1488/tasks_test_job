import hashlib

from sqlalchemy.exc import IntegrityError


from src.task.interfaces.user_interfaces import UserInterface
from src.task.schemas.auth_schemas import ResponseTokenLoginSchema
from src.task.schemas.user_schemas import UserBaseSchema


class UserServices:
    def __init__(self, user_repo: UserInterface) -> None:
        self.user_repo = user_repo()

    async def password_to_hash(self, user_input:UserBaseSchema) -> dict:
        '''Converts a password to a hash password'''

        user_dict = user_input.model_dump()
        hash_object = hashlib.sha256(user_dict['password'].encode())
        hash_password = hash_object.hexdigest()
        user_dict['password_hash'] = hash_password
        user_dict.pop('password')
        return user_dict

    async def user_registration(self, user_input: UserBaseSchema) -> bool:
        '''Creates a hash of the password and adds a new user to the users table'''
        user_dict = self.password_to_hash(user_input)
        try:
            await self.user_repo.add(user_dict)
            return True
        except IntegrityError:
            return False

    async def user_login(self, user_input: UserBaseSchema) -> ResponseTokenLoginSchema:
        '''Checks for user compliance and returns access_token and refresh_token'''





