from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from database import Base

class Member(Base):
    __tablename__ = "member"
    id = Column(Integer, primary_key=True,index=True)
    username = Column(String,index=True)
    password = Column(String,index=True)
    email = Column(Integer,index=True)
    phonenumber = Column(String,index=True)
    