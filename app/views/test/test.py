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
        test = HomeworkModel.query.filter_by().all()
        for te in test:
            print(te.id)
            print(te.homework_1_deadline)
            print(te.homework_2_deadline)
            print(te.homework_3_deadline)
            print(te.homework_4_deadline)
            print(te.homework_title)
            print(te.homework_description)
            print(te.homework_type)
            print(te.created_at)
