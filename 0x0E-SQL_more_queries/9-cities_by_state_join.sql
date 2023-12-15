-- lists all cities contained in the database hbtn_0d_usa
-- Each record should display: cities.id - cities.name - states.name

SELECT c.id, c.name, s.name
FROM hbtn_0d_usa.cities c JOIN hbtn_0d_usa.states s ON c.state_id = s.id ORDER BY c.id ASC; 
