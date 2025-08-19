from models import Base, Dog
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///dogs.db')
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

def create_table(base, engine):
    Base.metadata.create_all(engine)

def save(session, dog):
    session.add(dog)
    session.commit()
    return dog

def get_all(session):
    return session.query(Dog).all()

def find_by_name(session, name):
    return session.query(Dog).filter_by(name=name).first()

def find_by_id(session, id):
    return session.get(Dog, id)   # ✅ works in SQLAlchemy 2.0

def find_by_name_and_breed(session, name, breed):
    return session.query(Dog).filter_by(name=name, breed=breed).first()

def update_breed(session, dog, breed):
    dog.breed = breed
    session.commit()
    return dog

def delete(session, dog):
    session.delete(dog)
    session.commit()
