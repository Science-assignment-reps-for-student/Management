import os
import time

from flask import Blueprint, request
from flask_restful import Api, Resource
from sqlalchemy import and_

from app.services import user_type_checker, jwt_checker

from app.extension import db
from app.models.homework import HomeworkModel
from app.models.singlefiles import SinglefileModel
from app.models.multifiles import MultifileModel
from app.models.user import UserModel
from app.models.team import TeamModel
from app.models.members import MemberModel
from app.models.self_ev import SelfevaluationModel
from app.models.mutual_ev import MutualevaluationModel


api = Api(Blueprint(__name__,__name__))
api.prefix = "/tenderloin"

@api.resource("/admin/homework/team")
class experiment_homework(Resource):
    def get(self):
        type = user_type_checker(jwt_checker(request.headers["Authorization"][7:]))

        if not (type == 1 or type == 2): return {"message": "your not admin"}

        experiments = HomeworkModel.query.filter_by(homework_type=1).all()

        res = []

        for experiment in experiments:
            c_1, c_2, c_3, c_4 = [], [], [], []             # check
            users = UserModel.query.order_by(UserModel.user_number.asc()).all()
            for user in users:
                s_evaluation = SelfevaluationModel.query.filter(and_(
                    SelfevaluationModel.user_id == user.id,
                    SelfevaluationModel.homework_id == experiment.id
                )).first()

                m_evaluations = MutualevaluationModel.query.filter(and_(
                    MutualevaluationModel.user_id == user.id,
                    MutualevaluationModel.homework_id == experiment.id,
                )).count()
                print("1")

                member_count = 0
                l_1_a = MemberModel.query.filter_by(user_id=user.id).all()
                for l_1 in l_1_a:
                    t_1 = TeamModel.query.filter_by(id=l_1.team_id).first()
                    if t_1.homework_id == experiment.id:
                        member_count = MemberModel.query.filter_by(team_id=t_1.id).count()
                        break

                print("2")

                if m_evaluations == member_count and s_evaluation:
                    flag = False
                else: flag = True
                print("3")

                user_class = int(str(user.user_number)[1])
                if user_class == 1:
                    if flag:
                        c_1.append({
                            "user_name": user.user_name,
                            "user_number": user.user_number,
                            "submit": 0
                        })
                    else:
                        c_1.append({
                            "user_name": user.user_name,
                            "user_number": user.user_number,
                            "submit": 1
                        })
                elif user_class == 2:
                    if flag:
                        c_2.append({
                            "user_name": user.user_name,
                            "user_number": user.user_number,
                            "submit": 0
                        })
                    else:
                        c_2.append({
                            "user_name": user.user_name,
                            "user_number": user.user_number,
                            "submit": 1
                        })
                elif user_class == 3:
                    if flag:
                        c_3.append({
                            "user_name": user.user_name,
                            "user_number": user.user_number,
                            "submit": 0
                        })
                    else:
                        c_3.append({
                            "user_name": user.user_name,
                            "user_number": user.user_number,
                            "submit": 1
                        })
                elif user_class == 4:
                    if flag:
                        c_4.append({
                            "user_name": user.user_name,
                            "user_number": user.user_number,
                            "submit": 0
                        })
                    else:
                        c_4.append({
                            "user_name": user.user_name,
                            "user_number": user.user_number,
                            "submit": 1
                        })

            c_1_t, c_2_t, c_3_t, c_4_t = [], [], [], []
            teams = TeamModel.query.filter_by(homework_id=experiment.id).all()
            for team in teams:
                multifile = MultifileModel.query.filter_by(team_id=team.id).first()
                leader = UserModel.query.filter_by(id=team.leader_id).first()
                team_infos = MemberModel.query.filter_by(team_id=team.id).all()
                team_class = int(str(leader.user_number)[1])
                member = []

                for team_info in team_infos:
                    member_info = UserModel.query.filter_by(id=team_info.user_id).first()
                    member.append({
                        "member_name": member_info.user_name,
                        "member_number": member_info.user_number
                    })

                if team_class == 1:
                    if multifile is None:
                        c_1_t.append({
                            "team_name": team.team_name,
                            "leader_name": leader.user_name,
                            "leader_number": leader.user_number,
                            "team_info": member,
                            "submit": 0
                        })
                    else:
                        if multifile.late == False:
                            c_1_t.append({
                                "team_name": team.team_name,
                                "leader_name": leader.user_name,
                                "leader_number": leader.user_number,
                                "team_info": member,
                                "submit": 1
                            })
                        else:
                            c_1_t.append({
                                "team_name": team.team_name,
                                "leader_name": leader.user_name,
                                "leader_number": leader.user_number,
                                "team_info": member,
                                "submit": 2
                            })
                if team_class == 2:
                    if multifile is None:
                        c_2_t.append({
                            "team_name": team.team_name,
                            "leader_name": leader.user_name,
                            "leader_number": leader.user_number,
                            "team_info": member,
                            "submit": 0
                        })
                    else:
                        if multifile.late == False:
                            c_2_t.append({
                                "team_name": team.team_name,
                                "leader_name": leader.user_name,
                                "leader_number": leader.user_number,
                                "team_info": member,
                                "submit": 1
                            })
                        else:
                            c_2_t.append({
                                "team_name": team.team_name,
                                "leader_name": leader.user_name,
                                "leader_number": leader.user_number,
                                "team_info": member,
                                "submit": 2
                            })
                if team_class == 3:
                    if multifile is None:
                        c_3_t.append({
                            "team_name": team.team_name,
                            "leader_name": leader.user_name,
                            "leader_number": leader.user_number,
                            "team_info": member,
                            "submit": 0
                        })
                    else:
                        if multifile.late == False:
                            c_3_t.append({
                                "team_name": team.team_name,
                                "leader_name": leader.user_name,
                                "leader_number": leader.user_number,
                                "team_info": member,
                                "submit": 1
                            })
                        else:
                            c_3_t.append({
                                "team_name": team.team_name,
                                "leader_name": leader.user_name,
                                "leader_number": leader.user_number,
                                "team_info": member,
                                "submit": 2
                            })
                if team_class == 4:
                    if multifile is None:
                        c_4_t.append({
                            "team_name": team.team_name,
                            "leader_name": leader.user_name,
                            "leader_number": leader.user_number,
                            "team_info": member,
                            "submit": 0
                        })
                    else:
                        if multifile.late == False:
                            c_4_t.append({
                                "team_name": team.team_name,
                                "leader_name": leader.user_name,
                                "leader_number": leader.user_number,
                                "team_info": member,
                                "submit": 1
                            })
                        else:
                            c_4_t.append({
                                "team_name": team.team_name,
                                "leader_name": leader.user_name,
                                "leader_number": leader.user_number,
                                "team_info": member,
                                "submit": 2
                            })

            res.append({
                "homework_id": experiment.id,
                "homework_title": experiment.homework_title,
                "homework_description": experiment.homework_description,
                "created_at": time.mktime(experiment.created_at.timetuple()),
                "class_1": {
                    "deadline": time.mktime(experiment.homework_1_deadline.timetuple()),
                    "personal_submit_list": c_1,
                    "team_submit_list": c_1_t
                },
                "class_2": {
                    "deadline": time.mktime(experiment.homework_2_deadline.timetuple()),
                    "personal_submit_list": c_2,
                    "team_submit_list": c_2_t
                },
                "class_3": {
                    "deadline": time.mktime(experiment.homework_3_deadline.timetuple()),
                    "personal_submit_list": c_3,
                    "team_submit_list": c_3_t
                },
                "class_4": {
                    "deadline": time.mktime(experiment.homework_4_deadline.timetuple()),
                    "personal_submit_list": c_4,
                    "team_submit_list": c_4_t
                },
            })

        return {
            "homework_type": 1,
            "homework_info": res
        }, 200