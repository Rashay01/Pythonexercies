-- https://sqlbolt.com/lesson/introduction
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
SELECT name, role FROM employees
where Building is null;

SELECT * FROM employees
left join Buildings on employees.building = buildings.Building_name
where Years_employed =0

SELECT distinct Building_name 
FROM Buildings 
left join Employees on Building_name = Building
where Building is null

-- #9
SELECT title, (domestic_sales + international_sales) / 1000000 AS total_sales
FROM movies 
inner JOIN boxoffice ON id = movie_id;

SELECT title, ROUND((domestic_sales + international_sales) / 1000000,2) AS total_million_sales
FROM movies 
inner join boxoffice on id = movie_id;

SELECT title, Rating*10 AS rating_percentage
FROM movies 
inner join boxoffice on id = movie_id;

SELECT *
FROM movies
WHERE year % 2 = 0;

-- #10
SELECT Max(Years_employed) AS Max_Years_Employed FROM employees;

SELECT role, AVG(Years_employed) as Avg_years_employed 
FROM employees
group by role;

SELECT building, SUM(Years_employed) as Total_Years_Employed 
FROM employees
group by building;

-- #11
SELECT role, COUNT(*) as Number_of_artists
FROM employees
WHERE role = "Artist";

SELECT role, COUNT(*) as Number_of_emloyees
FROM employees
group by role;

SELECT role, SUM(Years_employed) as Total_years_emloyed
FROM employees
where role = "Engineer"
-- or
SELECT role, SUM(Years_employed) as Total_years_emloyed
FROM employees
group by role
having role = "Engineer";

-- Notes 
-- SELECT DISTINCT column, AGG_FUNC(column_or_expression), …
-- FROM mytable
--     JOIN another_table
--       ON mytable.column = another_table.column
--     WHERE constraint_expression
--     GROUP BY column
--     HAVING constraint_expression
--     ORDER BY column ASC/DESC
--     LIMIT count OFFSET COUNT;
-- 
-- #12

SELECT director, count(director) as num_movies
FROM movies
group by director;

SELECT director, sum(Domestic_sales + International_sales) as total_sales
FROM movies
inner join Boxoffice on id=Movie_id
group by director;


-- #13
INSERT INTO movies VALUES (15,"Toy Story 4", "John Lasseter", 2024, 90);

INSERT INTO boxoffice VALUES (15, 8.7, 340000000, 270000000);
-- or
INSERT INTO boxoffice (movie_id, rating, domestic_sales, international_sales)
VALUES (15, 8.7, 340000000, 270000000);


-- #14
UPDATE Movies
SET Director = "John Lasseter"
WHERE Title = "A Bug's Life"

UPDATE Movies
SET Year = 1999
WHERE Title = "Toy Story 2"

UPDATE Movies
SET Title = "Toy Story 3", Director = "Lee Unkrich"
WHERE Title = "Toy Story 8"

-- #15
DELETE from Movies
WHERE Year < 2005

SELECT * FROM movies 
WHERE Director = "Andrew Stanton";

DELETE from Movies
WHERE Director = "Andrew Stanton";

-- DML - INSERT, UPDATE, DELETE - ALTERs  
-- DDL Commands (Data Definition Language) 
-- ALter the table

-- Alter the tables's schema

-- INTEGER, BOOLEAN
-- FLOAT, DOUBLE, REAL
-- CHARACTER(num_of_chars), VARCHAR(num_of_chars) -> under 120 words, TEXT
-- DATE, DATETIME
-- BLOB -> Binary data
-- Below are table schema 

-- 16
CREATE TABLE Database (
    Name TEXT,
    Version FLOAT,
    Download_count INTEGER
);

CREATE TABLE IF NOT EXISTS Database (
    Name TEXT,
    Version FLOAT,
    Download_count INTEGER
);

-- 17 

ALTER TABLE Movies
ADD Aspect_ratio FLOAT

ALTER TABLE Movies
ADD Language TEXT 
DEFAULT "English"

-- 18
DROP TABLE IF EXISTS Movies;

DROP TABLE IF EXISTS Boxoffice;