from config import *

from langchain.prompts import PromptTemplate

# Quiz Generator template
quiz_content_generator_prompt = PromptTemplate(
    input_variables=["field", "quiz_options_number"],
    template="""
System: As an expert in {field}, your task is to create a multiple-choice quiz designed to evaluate the skills of potential hires for your company in this field. 
User: Please generate a quiz related to {field} to assess their skills.
Restriction: The quiz must contain {quiz_options_number} questions.
Restriction : The quiz must contain at least 4 options per question.
Restriction: The quiz must contain at least 1 correct answer per question.
Restriction: The quiz must be in  valid json format.

Quiz Format:
{{
 items : [
     {{
        "question": "...",
        "options": [
            {{
                "option": "...",
                "is_correct": "True/False",
            }}
            ...
        ]
    }}
 ]

}}
    ...

Quiz:

"""
)

