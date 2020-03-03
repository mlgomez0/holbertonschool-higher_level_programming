-- script that lists all the cities of California that can be found in the database hbtn_0d_usa.
-- states table contains only one record where name = California, Results must be sorted in ascending order by cities.id.
SELECT cities.id, cities.name from hbtn_0d_usa.cities WHERE hbtn_0d_usa.cities.state_id = (SELECT states.id from hbtn_0d_usa.states WHERE hbtn_0d_usa.states.name = "California") ORDER BY cities.id ASC;
