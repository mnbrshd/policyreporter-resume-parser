from pydantic import BaseModel, EmailStr
from typing import List

class ResumeData(BaseModel):
    name: str
    email: EmailStr
    skills: List[str]