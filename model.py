from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from .database import Base

class Address(Base):
    __tablename__ = "Address"
    id = Column(Integer, primary_key=True,index=True)
    store_name = Column(String,index=True)
    disctrict = Column(String,index=True)
    zip_code = Column(Integer,index=True)
    province = Column(String,index=True)
    