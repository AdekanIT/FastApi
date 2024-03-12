from fastapi import FastAPI
from api.user_api.users import user_router, user_answer_db, get_all_users_db
from api.question_api.question import question_router
from database import Base, engine

app = FastAPI(docs_url='/')
Base.metadata.create_all(bind=engine)

app.include_router(user_router)
app.include_router(question_router)


@app.get('/', tags=['Main page'])
async def home():
    return {'Hello': 'My Nigers'}









































































