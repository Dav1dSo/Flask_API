from pydantic import BaseModel

class HomeReponseSchema(BaseModel):
    msg: str
    
class HomeRequestSchema(BaseModel):
    user: int
    password: int