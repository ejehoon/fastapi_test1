from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DB_URL = 'mysql+pymysql://admin:00000000@database-2.cniyjmhourjo.ap-northeast-2.rds.amazonaws.com:3306/fastapi'

class engineconn:
    def __init__(self):
        self.engine = create_engine(DB_URL, pool_recycle=500)

    def sessionmaker(self):
        Session = sessionmaker(bind=self.engine)
        session = Session()
        return session

    def connection(self):
        conn = self.engine.connect()
        return conn
