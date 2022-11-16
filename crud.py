from sqlalchemy.orm import Session
import models, schemas

def get_all_member(db: Session):
    return db.query(models.Member).all()

def get_member_by_email(db: Session, email: str):
    return db.query(models.Member).filter(models.Member.email == email).first()

def get_member_by_username(db:Session,username: str):
    return db.query(models.Member).filter(models.Member.username == username).first()

def create_member(db: Session, member:schemas.MemberBase):
    db_member = models.Member(**member.dict())
    db.add(db_member)
    db.commit()
    db.refresh(db_member)
    return db_member

def update_member(db:Session, member:schemas.MemberBase, add_member:schemas.CreateMember):
    member.username = add_member.username
    member.password = add_member.password
    member.email = add_member.email
    member.phonenumber = add_member.phonenumber
    db.commit()
    db.refresh(member)
    return member

def delete_member(db:Session, member:schemas.Member):
    db.delete(member)
    db.commit()