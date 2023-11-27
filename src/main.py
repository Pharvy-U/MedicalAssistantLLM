from typing import Optional
from fastapi import FastAPI

from genericDTO import GenericDTO
from llm import converse


app = FastAPI()


@app.post('/chat')
def chat(request: GenericDTO):
    return converse(request.message)

@app.get('/report')
def report(num: int=4, sort: Optional[str] = None):
    return {'data': num}