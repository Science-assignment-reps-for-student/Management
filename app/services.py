import jwt

from config.app_config import TestAppConfig
from app.models.user import UserModel


def jwt_checker(token: str) -> int:
    return jwt.decode(token, TestAppConfig.SECRET_KEY)["user_id"]


def user_type_checker(user_id: int) -> int:
    return UserModel.query.filter_by(id=user_id).first().user_type