.read data.sql


CREATE TABLE bluedog AS
  SELECT color, pet
  FROM students
  WHERE color = 'blue' and pet = 'dog';

CREATE TABLE bluedog_songs AS
  SELECT color, pet, song
  FROM students
  WHERE color = 'blue' and pet = 'dog';


CREATE TABLE smallest_int AS
  SELECT time, smallest
  FROM students
  WHERE smallest > 2
  ORDER BY smallest;


CREATE TABLE matchmaker AS
  SELECT first.pet,first.song,first.color,second.color
  FROM students as first, students as second
  WHERE first.pet = second.pet and
		first.song = second.song and
		first.time < second.time;


CREATE TABLE sevens AS
  SELECT a.seven
  FROM students as a, numbers as b
  WHERE a.time = b.time and
		a.number = 7 and
		b."7" = "True";

