-- lists all cities contained in the database hbtn_0d_usa
-- each record should display: cities.id - cities.name - states.name
-- you can use only one select statement
SELECT cities.id, cities.name, states.name FROM cities LEFT JOIN states ON cities.state_id = states.id ORDER BY states.id;
