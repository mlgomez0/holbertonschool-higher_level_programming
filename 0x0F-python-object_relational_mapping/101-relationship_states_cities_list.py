#!/usr/bin/python3
"""script that lists all State objects from the database hbtn_0e_6_usa
"""
import sys
from relationship_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import (create_engine)
from relationship_city import City

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localho\
st/{}'.format(sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    se = Session()
    q = se.query(State, City).join(City)\
        .order_by(State.id).order_by(City.id)
    name_l = ""
    for i in q:
        if name_l != i.State.name:
            print("{:d}: {:s}".format(i.State.id, i.State.name))
            name_l = i.State.name
        print("    {:d}: {:s}".format(i.City.id, i.City.name))
