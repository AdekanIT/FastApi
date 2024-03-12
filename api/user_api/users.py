from fastapi import APIRouter
from database.user_service import registration_db, user_answer_db, get_all_users_db, points_db
from database.question_service import get_questions_db, add_question_db, top_5_db

user_router = APIRouter(prefix='/user', tags=['Methods for users'])


@user_router.post('/register')
async def register(name: str, phone_number: int, level: str):
    regist = registration_db(name, phone_number, level)
    return f'You successfully registered {regist}'


@user_router.get('/answers')
async def user_answers(user_id: int, question_id: int, level: str, user_answer: str):
    answer = user_answer_db(user_id, question_id, level, user_answer)
    return f'Your answers {answer}'


@user_router.get('/all-users')
async def get_all_user():
    return get_all_users_db()


@user_router.post('/points')
async def points_all(user_id: int, correct_answers: int):
    points = points_db(user_id, correct_answers)
    return f'Points: {points}'