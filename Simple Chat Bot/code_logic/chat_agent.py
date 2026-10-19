# This code base is responsible for chat
from ollama import chat
from config import *
from config_llm.std_str_prompt import SYSTEM_PROMPT


class bot:
    def __init__(self) -> None:
        pass

    def chat_fun(self, user_input_str=None,history=None):
        try:
            response=chat(
                model=BASE_MODEL,
                messages=history or [
                    {'role':'system','content':SYSTEM_PROMPT},
                    {'role':'user','content':user_input_str}
                ]
            )
            return response["message"]["content"]
        except :
            return "Error"
