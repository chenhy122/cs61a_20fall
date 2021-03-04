.read data.sql


CREATE TABLE average_prices AS
  SELECT category, AVG(MSRP) as average_price
  FROM products
  GROUP BY category;


CREATE TABLE lowest_prices AS
  SELECT store, item, MIN(price)
  FROM inventory
  GROUP BY item;


CREATE TABLE shopping_list AS
  SELECT name, store
  FROM products, lowest_prices
  WHERE name = item
  GROUP BY category
  HAVING MIN(MSRP/rating);


CREATE TABLE total_bandwidth AS
  SELECT SUM(b.Mbs)
  FROM shopping_list as a, stores as b
  WHERE a.store = b.store;

