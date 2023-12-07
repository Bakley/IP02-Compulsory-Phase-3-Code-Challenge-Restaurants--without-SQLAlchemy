from sqlalchemy import (create_engine, desc,
    CheckConstraint, PrimaryKeyConstraint, UniqueConstraint,
    Index, Column, DateTime, Integer, String)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


# create an sqlite database engine
engine = create_engine('sqlite:///mydb_one.db')

# Declare a base class using SQLAlchemy
Base = declarative_base()

# Defining a python class as a model for the Players table
class Player(Base):
    
    __tablename__ = 'Koins'
    
    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)
    age = Column(Integer)
        


        
if __name__ == "__main__":
    
    # Create the tables
    Base.metadata.create_all(engine)

    # Session
    Session = sessionmaker(bind=engine)
    session = Session()
    user1 = Player(name="Haroun", email="j@doe.com", age=30)
    # user2 = Player("Mwau", "jane@doe.com", 30)
    
    session.add(user1)
    session.commit()
    
    
    # print(user1)
    user_in_system = session.query(Player).filter_by()
    for user in user_in_system:
        print(user.name)
    
    # user2.insert_user_obj_to_db()
    # # print(user2)
    
    # user_from_db = Player.view_user_obj('Haroun')
    # print(user_from_db)