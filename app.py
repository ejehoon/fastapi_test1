from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from database import engineconn
from models import Test, User

app = FastAPI()

# 데이터베이스 엔진 인스턴스 생성
engine = engineconn().engine

# 의존성 주입을 위한 세션 생성 함수
def get_db():
    db = Session(bind=engine)
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/test")
def get_test_data(db: Session = Depends(get_db)):
    return db.query(Test).all()

@app.get("/users")
def get_users(db: Session = Depends(get_db)):
    return db.query(User).all()
