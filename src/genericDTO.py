from pydantic import BaseModel


class GenericDTO(BaseModel):
    sender: str
    message: str