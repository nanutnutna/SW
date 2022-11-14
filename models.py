from sqlalchemy import Column, Integer, String
from database import Base

class Member(Base):
    __tablename__ = "member"
    id = Column(Integer, primary_key=True,index=True)
    username = Column(String,index=True)
    password = Column(String,index=True)
    email = Column(String,index=True)
    phonenumber = Column(String,index=True)
