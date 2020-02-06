import os
import time

from flask import Blueprint
from flask_restful import Api, Resource

from app.extension import db
from app.models.homework import HomeworkModel


api = Api(Blueprint(__name__,__name__))

@api.resource("/admin/homework/personal")
class personal_homework(Resource):
    def get(self):
        personal_homeworks = HomeworkModel.query.filter_by(homework_type=0).all()

        res = []

        for personal_homework in personal_homeworks:
            res.append({
                "homework_id": personal_homework.id,
                "homework_title": personal_homework.homework_title,
                "homework_description": personal_homework.homework_description,
                "created_at": time.mktime(personal_homework.created_at.timetuple()),
                "class_1": {
                    "deadline": personal_homework.homework_1_deadline,
                },
            })

        print(res)

        return {
            "homework_type": 0,
            "homework_info": res
        }, 200