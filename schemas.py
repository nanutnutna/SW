from pydantic import BaseModel


class MemberBase(BaseModel):
    username: str
    password: str
    email: str
    phonenumber: str


class Member(MemberBase):
    id: int
    class Config:
        orm_mode = True

