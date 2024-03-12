from database.models import *
from database import get_db


def top_5_db():
    db = next(get_db())
    leaders = db.query(Result.user_id).order_by(Result.correct_answers.desc())
    return leaders[:5]


def add_question_db(q_text, v1, v2, v3, v4, correct_answer):
    db = next(get_db())
    new_question = Question(q_text=q_text, v1=v1, v2=v2, v3=v3, v4=v4, correct_answer=correct_answer)
    db.add(new_question)
    db.commit()
    return 'Question added!'


def get_questions_db():
    db = next(get_db())

    question = db.query(Question).all()
    return question[:20]