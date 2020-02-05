import os
import time

from flask import Blueprint
from flask_restful import Api, Resource

from app.extension import db
from app.models.homework import HomeworkModel


api = Api(Blueprint(__name__,__name__))

@api.resource("/test")
class test(Resource):
    def get(self):
        test = HomeworkModel(
            homework_1_deadline = time.gmtime(time.time()),
            homework_2_deadline = time.gmtime(time.time()),
            homework_3_deadline = time.gmtime(time.time()),
            homework_4_deadline = time.gmtime(time.time()),
            homework_title = "TestTitle",
            homework_description = "testdescription",
            homework_type = 1,
            created_at = time.gmtime(time.time())
        )
        db.session.add(test)
        db.session.commit()