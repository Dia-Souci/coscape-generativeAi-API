import pydantic
from typing import List, Dict
from enums import *


    
# GENERATION PARAMS



class QuizRequestBody(pydantic.BaseModel):
    field: str = "Marketing"
    quiz_options_number: int = 4

class QuizOption(pydantic.BaseModel):
    option: str
    is_correct: bool
class QuizItem(pydantic.BaseModel):
    question: str
    options: List[QuizOption]
class Quiz(pydantic.BaseModel):
    items: List[QuizItem]
