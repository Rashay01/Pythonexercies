SELECT * FROM movies
where id = 6;

SELECT * FROM movies
where year between 2000 and 2010;

SELECT * FROM movies
WHERE year NOT BETWEEN 2000 and 2010;

SELECT * FROM movies
WHERE id < 6;

SELECT title, year FROM movies
WHERE year <= 2003;

-- Ex3
SELECT * FROM movies
where title like "Toy Story%"

SELECT * FROM movies
where director = "John Lasseter"

SELECT * FROM movies
where director != "John Lasseter"

SELECT * FROM movies
WHERE Title like "WALL-%"

-- #4
SELECT distinct director FROM movies
ORDER BY director ASC

SELECT * FROM movies
ORDER BY year DESC
LIMIT 4;

SELECT * FROM movies
ORDER BY Title ASC
LIMIT 5;

SELECT * FROM movies
ORDER BY Title ASC
LIMIT 5 OFFSET 5;

-- #5

SELECT * FROM north_american_cities
where Country = "Canada"

SELECT city, latitude FROM north_american_cities
WHERE country = "United States"
ORDER BY latitude DESC;

SELECT * FROM north_american_cities
WHERE longitude < -87.629798
ORDER BY longitude ASC;

SELECT * FROM north_american_cities
WHERE longitude < (select longitude from north_american_cities where city = "Chicago")
ORDER BY longitude ASC;

SELECT * FROM north_american_cities
WHERE country = "Mexico"
ORDER BY Population DESC
LIMIT 2

SELECT * FROM north_american_cities
WHERE country = "United States"
ORDER BY Population DESC
LIMIT 2 OFFSET 2

-- #6

SELECT Title, Domestic_sales,International_sales FROM movies
INNER JOIN Boxoffice ON movies.Id =Boxoffice.Movie_id

SELECT title, domestic_sales, international_sales
FROM movies 
INNER JOIN boxoffice ON movies.id = boxoffice.movie_id
WHERE domestic_sales < international_sales;

SELECT title, rating
FROM movies 
INNER JOIN boxoffice ON movies.id = boxoffice.movie_id
ORDER BY rating DESC;

-- #7
SELECT distinct building FROM employees;

SELECT * FROM buildings;

SELECT distinct building_name, role 
FROM buildings 
LEFT JOIN employees ON building_name = building;

-- #8
SELECT * FROM employees
where Years_employed =0

SELECT * FROM employees
left join Buildings on employees.building = buildings.Building_name
where Years_employed =0

SELECT distinct Building_name 
FROM Buildings 
left join Employees on Building_name = Building
where Building is null