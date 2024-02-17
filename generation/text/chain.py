from langchain.chains import LLMChain
from generation.text.llm import chatGPT
from generation.text.prompt import *




quiz_content_generator = LLMChain(llm=chatGPT, prompt=quiz_content_generator_prompt)