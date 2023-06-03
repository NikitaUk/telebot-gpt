from sqlalchemy import create_engine, Column, Integer, String, text
from sqlalchemy.orm import declarative_base, create_session
import config

try:
    engine = create_engine(config.ENGINE)
    Base = declarative_base()
    session = create_session(bind=engine)
except:
    print("Не удалось подключится к базе данных")

class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True, autoincrement=True)
    client_id = Column(String, nullable=False)
    login = Column(String(11), nullable=False)

def loginUser(chat_id):
    request = text(f"SELECT * FROM public.user WHERE client_id = '133870350'")
    # request = text(f"SELECT * FROM public.user WHERE client_id = '{chat_id}'")
    querry = session.execute(request).fetchall()
    session.commit()
    session.close()
    res = False
    if len(querry) > 0:
        res = True 
    else:
        res = False
    return res

#Base.metadata.create_all(engine)