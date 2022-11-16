from fastapi import FastAPI,Depends,HTTPException
from sqlalchemy.orm import Session
import crud,models,schemas
from database import SessionLocal,engine
from typing import List
app = FastAPI()

models.Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/users/",response_model=schemas.Member)
def create_member(member: schemas.MemberBase, db:Session = Depends(get_db)):
    db_email = crud.get_member_by_email(db, email=member.email)
    if db_email:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_member(member=member,db=db)

@app.get("/usersall/",response_model=List[schemas.Member])
def read_member(db:Session=Depends(get_db)):
    users = crud.get_all_member(db)
    return users

@app.get('/user/{username}',response_model=schemas.Member)
def read_member_id(username: str , db:Session = Depends(get_db)):
    db_username = crud.get_member_by_username(db=db,username=username)
    if db_username is None :
        raise HTTPException(status_code=404, detail="User does not exist")
    return db_username

@app.put('/user/{username}',response_model=schemas.Member)
def update_member(username: str, add_member: schemas.CreateMember, db:Session = Depends(get_db)):
    db_username = crud.get_member_by_username(db=db,username=username)
    if db_username is None :
        raise HTTPException(status_code=404, detail="User does not exist")
    return crud.update_member(db=db,member=db_username,add_member=add_member)

@app.delete('/user/{username}',response_model=schemas.Member)
def delete_member(username: str, db:Session = Depends(get_db)):
    db_member = crud.get_member_by_username(db, username=username)
    if db_member is None :
        raise HTTPException(status_code=404, detail="User does not exist")
    crud.delete_member(db=db, member=db_member)
    return "Successfully deleted the user"

## delete , update_user , get_by_user