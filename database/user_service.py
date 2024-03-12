from .models import Users, UserAnswer, Question, Result
from datetime import datetime

from database import get_db


def registration_db(name, phone_number, level):
    db = next(get_db())
    checker = db.query(Users).filter_by(phone_number=phone_number).first()
    if checker:
        return checker.id
    else:
        new_user = Users(name=name, phone_number=phone_number, level=level, created_at=datetime.now())
        db.add(new_user)
        db.commit()
        return new_user.id


def get_all_users_db():
    db = next(get_db())
    info_all = db.query(Users).all()
    return info_all


def user_answer_db(user_id, question_id, level, user_answer):
    db = next(get_db())
    exact_question = db.query(Question).filter_by(id=question_id).first()
    if exact_question:
        if exact_question.correct_answer == user_answer:
            correct_answers = True
        else:
            correct_answers = False

        new_answer = UserAnswer(user_id=user_id,
                                q_id=question_id,
                                level=level,
                                user_answer=user_answer,
                                correct_answers=correct_answers)
        db.add(new_answer)
        db.commit()
        return True if correct_answers else False
    else:
        return 'Answer not found!'


def points_db(user_id, correct_answers):
    db = next(get_db())
    checker = db.query(Result).filter_by(user_id=user_id).first()
    if checker:
        checker.correct_answers += correct_answers
    else:
        new_leader_data = Result(user_id=user_id,
                                 correct_answers=correct_answers)
        db.add(new_leader_data)
        db.commit()

        all_leaders = db.query(Result.user_id).order_by(Result.correct_answers.desc())
        return all_leaders.index((user_id, ))





















































































