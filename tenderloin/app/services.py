import jwt

from tenderloin.config.app_config import ProductionAppconfig
from tenderloin.app.models.user import UserModel


def jwt_checker(token: str) -> int:
    return jwt.decode(token, TestAppConfig.SECRET_KEY)["user_id"]


def user_type_checker(user_id: int) -> int:
    return UserModel.query.filter_by(id=user_id).first().user_type
