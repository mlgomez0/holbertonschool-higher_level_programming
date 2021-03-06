#!/usr/bin/python3
"""script that lists all State objects from the database hbtn_0e_6_usa
"""
import sys
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy.orm import relationship, aliased
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localho\
st/{}'.format(sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    se = Session()
    new_state = State(name='California', cities=[City(name='San Francisco')])
    se.add(new_state)
    se.commit()
