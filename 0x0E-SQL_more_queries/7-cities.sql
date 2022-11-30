-- creates the database hbtn_0d_usa and the table cities
create database if not exists hbtn_0d_usa;
create table if not exists hbtn_0d_usa.cities (
	id int not null primary key auto_increment,
	state_id int not null,
	name varchar(256) not null,
	foreign key(state_id_ references hbtn_0d_usa.states(id)
);
