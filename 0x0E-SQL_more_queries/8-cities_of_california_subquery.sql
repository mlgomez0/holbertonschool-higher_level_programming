-- script that lists all the cities of California that can be found in the database hbtn_0d_usa.
-- states table contains only one record where name = California, Results must be sorted in ascending order by cities.id.
SELECT id, name from cities WHERE state_id = (SELECT id from states WHERE name = "California") ORDER BY id ASC;
