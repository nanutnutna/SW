from sqlalchemy.orm import Session
import models, schemas

def get_user(db: Session, user_id: int):
    return db.query(models.Member).filter(models.Member.username == user_id).first()

def get_user_by_email(db: Session, email: str):
    return db.query(models.Member).filter(models.Member.email == email).first()

def create_user(db: Session, user:schemas.MemberCreate):
    hashed_password = user.password + 'test'
    db_user = models.Member(email=user.email,hashed_password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user