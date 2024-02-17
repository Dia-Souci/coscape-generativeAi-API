import uuid
from generation.text.chain import *
from utils import *
from validate import *


def generate_quiz_content(**kwargs):
    quiz_str = quiz_content_generator.run(
        field=kwargs["field"],
        quiz_options_number=kwargs["quiz_options_number"],
    ).replace("\n", " ")
    if(is_json(quiz_str)):
        quiz = eval(quiz_str)
        quiz["id"] = str(uuid.uuid4())
        return quiz
    else:
        raise Exception("Quiz is not a valid JSON object")

