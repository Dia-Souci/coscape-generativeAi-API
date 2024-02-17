import os
import json

from models import *
from config import *
from generation.text.generate import *

from typing import List

from fastapi import FastAPI, HTTPException

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World!"}


@app.post("/quiz")
async def generate_quiz(request_body: QuizRequestBody) -> Quiz:
    quiz = generate_quiz_content(
        field = request_body.field,
        quiz_options_number = request_body.quiz_options_number
    )
    return Quiz(**quiz)
