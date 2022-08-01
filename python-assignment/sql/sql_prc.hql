show databases;
use ineuron;
create table IF NOT exists bank_details (
age int,
job  varchar (30),
marital  varchar (30),
education  varchar (30),
`default`  varchar (30),
balance  varchar (30),
housing  varchar (30),
loan   varchar (30),
contact   varchar (30),
`day`  int,
`month`  varchar (30),
duration  int,
campaign  int,
pdays  int,
previous  int,
poutcome  varchar (30),
y  varchar (30));

select * from bank_details;

Describe bank_details; 
insert into bank_details values (58,"management","married","tertiary","no",2143,"yes","no","unknown",5,"may",261,1,-1,0,"unknown","no");

select * from bank_details;


select distinct age,job from bank_details;

select `default`,job from bank_details;

select distinct * from bank_details where job = 'retired' and balance >100;

select * from bank_details order by age;

select count(*) from bank_details;

select sum(balance)  from bank_details;

select avg(balance)  from bank_details;

select min(balance)  from bank_details;

#Nested qwery
select * from bank_details where balance = (select min(balance) from bank_details);

select count(*), marital from bank_details group by marital;

select count(*), marital, sum(balance), avg(balance) from bank_details group by marital

select count(*), marital, sum(balance), avg(balance) from bank_details group by marital having sum(balance) > 3000


set sql_safe_updates=0;

update bank_details set balance =0 where job='Unknown';

select * from bank_details;

update bank_details set contact='known' , y='yes' where month = 'may';

update bank_details set `default` = 'NULL' where `default` ='no';

delete from  bank_details where job='unknown';

#functions in sql are procedures