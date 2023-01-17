-- lists the cities i california from database
SELECT cities.id, cities.name
FROM cities, states
WHERE cities.state_id=states.id AND states.name="Californis"
ORDER BY cities.id ASC;