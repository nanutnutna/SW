from typing import Optional,List
from pydantic import BaseModel


class MemberBase(BaseModel):
    email: str
    phonenumber: str

class MemberCreate(MemberBase):
    password: str

class Member(MemberBase):
    id: int
    username: str
    class Config:
        orm_mode = True