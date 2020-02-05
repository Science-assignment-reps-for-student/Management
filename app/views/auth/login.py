import os

from flask import Blueprint, request, abort
from flask_restful import Api, Resource
from flask_jwt_extended import create_access_token


api = Api(Blueprint(__name__,__name__))

@api.resource("/admin/auth")
class admin_login(Resource):
    def post(self):
        id = request.json["id"]
        pw = request.json["pw"]

        # admin_id = os.getenv("ADMIN_ID")
        # admin_pw = os.getenv("ADMIN_PW")
        admin_id = "testadmin"
        admin_pw = "testadmin"


        if not admin_id == id or not admin_pw == pw:
            abort(409)

        return {
            "access_token": create_access_token(identity="admin_"+admin_id)
        }