#0x0F. Python - Object-relational mapping.
Educational project

#Concepts explored

- How to connect to a MySQL database from a Python script
- How to SELECT rows in a MySQL table from a Python script
- How to INSERT rows in a MySQL table from a Python script
- What ORM means
- How to map a Python Class to a MySQL table

#Installation

- All the files will be interpreted/compiled on Ubuntu 14.04 LTS using python3 (version 3.4.3).

```bash (example)
.  cat 0-select_states.sql | mysql -uroot -p
```

## Usage

Educational purposes

## Tasks (to run the script values has to be passed as arguments)
0. 0-select_states.py: script that lists all states from the database hbtn_0e_0_usa ( 3 arguments: mysql username, mysql password and database name, use the module MySQLdb, connect to a MySQL server running on localhost at port 3306, Results must be sorted in ascending order by states.id)
1. 1-filter_states.py: lists all states with a name starting with N (upper N) from the database hbtn_0e_0_usa hbtn_0e_0_usa ( 3 arguments: mysql username, mysql password and database name, use the module MySQLdb, connect to a MySQL server running on localhost at port 3306,     Results must be sorted in ascending order by states.id)
2. 2-my_filter_states.py:script that takes in an argument and displays all values in the states table of hbtn_0e_0_usa (where name matches the argument, 4 arguments: mysql username, mysql password, database name and state name searched, module MySQLdb, script should connect to a MySQL server running on localhost at port 3306, use format to create the SQL query with the user input, Results must be sorted in ascending order by states.id)
3. 3-my_safe_filter_states.py: script that takes in arguments and displays all values in the states table of hbtn_0e_0_usa where name matches the argument. But this time, write one that is safe from MySQL injections! (script should take 4 arguments: mysql username, mysql password, database name and state name searched (safe from MySQL injection), module MySQLdb, script should connect to a MySQL server running on localhost at port 3306m, Results must be sorted in ascending order by states.id
4. 4-cities_by_state.py:  script that lists all cities from the database hbtn_0e_4_usa(script should take 3 arguments: mysql username, mysql password and database name, module MySQLdb, script should connect to a MySQL server running on localhost at port 3306, sorted in ascending order by cities.id, allowed to use execute()).
5. 5-filter_cities.py: script that takes in the name of a state as an argument and lists all cities of that state, using the database hbtn_0e_4_usa( script should take 4 arguments: mysql username, mysql password, database name and state name (SQL injection free!), module MySQLdb, cript should connect to a MySQL server running on localhost at port 3306, Results must be sorted in ascending order by cities.id, can use only execute())..
6. model_state.py: python file that contains the class definition of a State and an instance Base = declarative_base():(State class: inherits from Base Tips, links to the MySQL table states, class attribute id that represents a column of an auto-generated, unique integer, cant be null and is a primary key, class attribute name that represents a column of a string with maximum 128 characters and cant be null, You must use the module SQLAlchemy, Your script should connect to a MySQL server running on localhost at port 3306
7. 7-model_state_fetch_all.py: script that lists all State objects from the database hbtn_0e_6_usa(Script should take 3 arguments: mysql username, mysql password and database name, You must use the module SQLAlchemy, You must import State and Base from model_state - from model_state import Base, State, script should connect to a MySQL server running on localhost at port 3306, Results must be sorted in ascending order by states.id.
8. 8-model_state_fetch_first.py: script that prints the first State object from the database hbtn_0e_6_usa(script should take 3 arguments: mysql username, mysql password and database name, module SQLAlchemy, import State and Base from model_state - from model_state import Base, State, script should connect to a MySQL server running on localhost at port 3306, state must be the first in states.id).
9. 9-model_state_filter_a.py: script that lists all State objects that contain the letter a from the database hbtn_0e_6_usa(script should take 3 arguments: mysql username, mysql password and database name, module SQLAlchemy, import State and Base from model_state - from model_state import Base, State, connect to a MySQL server running on localhost at port 3306, results must be sorted in ascending order by states.id.
10. 10-model_state_my_get.py: script that prints the State object with the name passed as argument from the database hbtn_0e_6_usa(script should take 4 arguments: mysql username, mysql password, database name and state name to search (SQL injection free), module SQLAlchemy, import State and Base from model_state - from model_state import Base, State, script should connect to a MySQL server running on localhost at port 3306, assumes to have one record with the state name to search, results must display the states.id.
11. 11-model_state_insert.py: script that adds the State object Louisiana to the database hbtn_0e_6_usa(script should take 3 arguments: mysql username, mysql password and database name, module SQLAlchemy, import State and Base from model_state - from model_state import Base, State, script should connect to a MySQL server running on localhost at port 3306, print the new states.id after creation.
12. 12-model_state_update_id_2.py: script that changes the name of a State object from the database hbtn_0e_6_usa(script should take 3 arguments: mysql username, mysql password and database name, module SQLAlchemy, import State and Base from model_state - from model_state import Base, State, script should connect to a MySQL server running on localhost at port 3306, change the name of the State where id = 2 to New Mexico.
13. 13-model_state_delete_a.py: script that deletes all State objects with a name containing the letter a from the database hbtn_0e_6_usa(script should take 3 arguments: mysql username, mysql password and database name, module SQLAlchemy, import State and Base from model_state - from model_state import Base, State, script should connect to a MySQL server running on localhost at port 3306.
14. model_city.py, 14-model_city_fetch_by_state.py: Write a Python file similar to model_state.py named model_city.py that contains the class definition of a City.
City class:
inherits from Base (imported from model_state)
links to the MySQL table cities
class attribute id that represents a column of an auto-generated, unique integer, cant be null and is a primary key
class attribute name that represents a column of a string of 128 characters and cant be null
class attribute state_id that represents a column of an integer, cant be null and is a foreign key to states.id
You must use the module SQLAlchemy
Next, write a script 14-model_city_fetch_by_state.py that prints all City objects from the database hbtn_0e_14_usa:
Your script should take 3 arguments: mysql username, mysql password and database name
You must use the module SQLAlchemy
You must import State and Base from model_state - from model_state import Base, State
Your script should connect to a MySQL server running on localhost at port 3306
Results must be sorted in ascending order by cities.id
Results must be display as they are in the example below (<state name>: (<city id>) <city name>).
