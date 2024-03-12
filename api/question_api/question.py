from fastapi import APIRouter
from database.user_service import user_answer_db
from database.question_service import get_questions_db, add_question_db

question_router = APIRouter(prefix='/question', tags=['Methods for questions'])


@question_router.get('/all-question')
async def all_questions_20():
    return get_questions_db()


@question_router.post('/add-question')
async def add_question(q_text: str, v1: str, v2: str, v3: str, v4: str, correct_answer: int):
    new_question = add_question_db(q_text, v1, v2, v3, v4, correct_answer)
    return new_question


@question_router.get('/get-user-answer')
def get_answers(user_id: int, question_id: int, level: str, user_answer: int):
    u_answer = user_answer_db(user_id, question_id, level, user_answer)
    return f'Action done {u_answer}'