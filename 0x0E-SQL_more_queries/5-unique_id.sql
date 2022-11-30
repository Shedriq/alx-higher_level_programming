-- create table 'unique_id'
-- id INT default 1 unique, name VARCHAR(256)
-- if table already exists, script should not fail
create tabl if not exists unique_id
(
	id INT DEFAULT 1 UNIQUE,
	name VARCHAR(256)
);
