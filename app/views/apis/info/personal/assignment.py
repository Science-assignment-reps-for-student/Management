import time

from flask import Blueprint, request
from flask_restful import Api, Resource
from sqlalchemy import and_

from app.models.homework import HomeworkModel
from app.models.singlefiles import SinglefileModel
from app.models.user import UserModel

from app.services import jwt_checker, user_type_checker


api = Api(Blueprint(__name__,__name__))
api.prefix = "/tenderloin"

@api.resource("/admin/homework/personal")
class personal_homework(Resource):
    def get(self):
        type = user_type_checker(jwt_checker(request.headers["Authorization"][7:]))

        if not (type == 1 or type == 2): return {"message":"your not admin"}

        personal_homeworks = HomeworkModel.query.filter_by(homework_type=0).all()

        res = []

        for personal_homework in personal_homeworks:
            c_1, c_2, c_3, c_4 = [], [], [], []
            users = UserModel.query.order_by(UserModel.user_number.asc()).all()
            for user in users:
                singlefiles = SinglefileModel.query.filter(and_(
                    SinglefileModel.homework_id == personal_homework.id,
                    SinglefileModel.user_id == user.id)
                ).first()
                user_class = int(str(user.user_number)[1])
                if user_class == 1:
                    if singlefiles is None: c_1.append({
                            "user_name": user.user_name,
                            "user_number": user.user_number,
                            "submit": 0
                        })
                    else:
                        if singlefiles.late == False:
                            c_1.append({
                                "user_name": user.user_name,
                                "user_number": user.user_number,
                                "submit": 1
                            })
                        else:
                            c_1.append({
                                "user_name": user.user_name,
                                "user_number": user.user_number,
                                "submit": 2
                            })
                elif user_class == 2:
                    if singlefiles is None:
                        c_2.append({
                            "user_name": user.user_name,
                            "user_number": user.user_number,
                            "submit": 0
                        })
                    else:
                        if singlefiles.late == False:
                            c_2.append({
                                "user_name": user.user_name,
                                "user_number": user.user_number,
                                "submit": 1
                            })
                        else:
                            c_2.append({
                                "user_name": user.user_name,
                                "user_number": user.user_number,
                                "submit": 2
                            })
                elif user_class == 3:
                    if singlefiles is None:
                        c_3.append({
                            "user_name": user.user_name,
                            "user_number": user.user_number,
                            "submit": 0
                        })
                    else:
                        if singlefiles.late == False:
                            c_3.append({
                                "user_name": user.user_name,
                                "user_number": user.user_number,
                                "submit": 1
                            })
                        else:
                            c_3.append({
                                "user_name": user.user_name,
                                "user_number": user.user_number,
                                "submit": 2
                            })
                elif user_class == 4:
                    if singlefiles is None:
                        c_4.append({
                            "user_name": user.user_name,
                            "user_number": user.user_number,
                            "submit": 0
                        })
                    else:
                        if singlefiles.late == False:
                            c_4.append({
                                "user_name": user.user_name,
                                "user_number": user.user_number,
                                "submit": 1
                            })
                        else:
                            c_4.append({
                                "user_name": user.user_name,
                                "user_number": user.user_number,
                                "submit": 2
                            })

            res.append({
                "homework_id": personal_homework.id,
                "homework_title": personal_homework.homework_title,
                "homework_description": personal_homework.homework_description,
                "created_at": time.mktime(personal_homework.created_at.timetuple()),
                "class_1": {
                    "deadline": time.mktime(personal_homework.homework_1_deadline.timetuple()),
                    "submit_list": c_1
                },
                "class_2": {
                    "deadline": time.mktime(personal_homework.homework_2_deadline.timetuple()),
                    "submit_list": c_2
                },
                "class_3": {
                    "deadline": time.mktime(personal_homework.homework_3_deadline.timetuple()),
                    "submit_list": c_3
                },
                "class_4": {
                    "deadline": time.mktime(personal_homework.homework_4_deadline.timetuple()),
                    "submit_list": c_4
                },
            })

        return {
            "homework_type": 0,
            "homework_info": res
        }, 200