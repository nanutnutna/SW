from sqlalchemy.orm import Session
import models, schemas

def get_user(db: Session, user_id: int):
    return db.query(models.Member).filter(models.Member.username == user_id).first()

def get_user_by_email(db: Session, email: str):
    return db.query(models.Member).filter(models.Member.email == email).first()

def create_member(db: Session, member:schemas.MemberBase):
    db_member = models.Member(**member.dict())
    db.add(db_member)
    db.commit()
    db.refresh(db_member)
    return db_member