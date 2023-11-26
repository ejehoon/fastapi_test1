from sqlalchemy import Column, String, Text, Integer, BigInteger
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = "users"

    uid = Column(String(255), primary_key=True)
    email = Column(String(255), nullable=True)
    photoURL = Column(Text, nullable=True)
    displayName = Column(String(255), nullable=True)

class Test(Base):
    __tablename__ = "test"

    id = Column(BigInteger, nullable=False, autoincrement=True, primary_key=True)
    name = Column(Text, nullable=False)
    number = Column(Integer, nullable=False)
