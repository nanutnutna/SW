from fastapi import FastAPI,Depends,HTTPException
from sqlalchemy.orm import Session
import crud,models,schemas
from database import SessionLocal,engine
app = FastAPI()

models.Base.metadata.create_all(bind=engine)

## Deoendency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/users/",response_model=schemas.Member)
def create_member(member: schemas.MemberBase, db:Session = Depends(get_db)):
    #db_user = crud.get_user_by_email(db, email=user.email)
    #print(db_user)
    #if db_user:
    #raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_member(member=member,db=db)

@app.get("/user/",response_model=list[schemas.Member])
async def read_users(skip: int=0, limit: int=100, db:Session=Depends(get_db)):
    users = crud.get_user(db, skip=skip, limit=limit)
    return users
