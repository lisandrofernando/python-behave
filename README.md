# python-behave
# To run this repository through the terminal use: behave features/loginTest.feature
# To print something in python just use => print("Hello World")
# To define a variable in python simple write => a=3 is a variable type number, but there's no specific return type  





##### This section will be for SQL queries #####
# Regular expression in SQL: % any character _ stands for single character
# select name from city where countrycode like 'A%'
# select countrycode from city where countrycode lile '__T%'
# select countrycode from city where countrycode lile '_A%'

# Get the names by alphabethical order or sort
# select * from employeeinfo order by name;
# select * from employeeinfo order by id;
# select * from employeeinfo order by id desc;
# Unique Names in EmployeeTable

# select distinct name from employeeinfo;

# get the employees name of newyork

# select name from employeeinfo where location='newyork';

# get the employees name of newyork where there age should be more than 23

# select name from employeeinfo where location='newyork' and age>23;

# get the employees name of Florida where there age should be less than 23 or location is from charlotte

# select name from employeeinfo where (location='florida' and age<23) or location='charlotte';

# select name from employeeinfo where id=1 or location ='florida';

# Print the employnames whose age should be between 22 and 25

# select name from employeeinfo where age in(22,23,24,25);

# select name from employeeinfo where location in('florida','newyork');

# print the emplyeenames whose id lies between 1 and 1000

# select name from employeeinfo where id between 1 and 1000;

# Aggregate function

# Problem: get total some of amount generated for each month

# select * from Transactions group by Month;
# select sum(amount), Month from Transactions group by Month;
# select Max(amount), Month from Transactions group by Month;
# select Max(amount), Month from Transactions;
# select Min(amount), Month from Transactions;
# select Min(amount), Month, branch from Transactions group by branch;
# select Avg(amount), Month, branch from Transactions group by branch;
# select count(*) from Transactions; the number of records retrieved
# select count(*), Month from Transactions group by Month having count(*)<2;
# select sum(amount), Month from Transactions where branch='' or branch='' group by Month;
# select sum(amount), Month from Transactions where branch='' or branch='' group by Month having sum(Amount)<500;
# select sum(amount), branch from Transactions where Month='feb' group by branch having sum(Amount)>4000;
# Subqueries
# select name, age from citizens where name=(select name from citizenloc where location='texas');
# select name, age from citizens where name in(select name from citizenloc where location='california');
# SQL Joins, and to join two tables use a common name in between the two tables
# select c.name, cl.location,c.age from citizens as c join citizenloc as cl on c.name=cl.name;  
# select c.name, cl.location,c.age from citizens as c join citizenloc as cl on c.name=cl.name where cl.location='california'; 
# select c.name, cl.location,c.age from citizens as c join citizenloc as cl on c.name=cl.name group by c.name having e.year= 1990;
# select c.name,e.year, sum(c.employees) from citizens as c join citizenloc as cl on c.name=cl.name group by c.name having e.year= 1990;
# select c.name,e.year, min(c.employees) from citizens as c join citizenloc as cl on c.name=cl.name group by c.name having e.year> 1990;
# select s.name, s.id, s.gender, s.grade, g.grade from student s inner join grades g on s.id=g.id;

# select s.name, s.id, s.gender, s.grade, g.grade from student s left join grades g on s.id=g.id;

# select s.name, s.id, s.gender, s.grade, g.grade from student s right join grades g on s.id=g.id;

# select s.name, s.id, s.gender, s.grade, g.grade from student s inner join grades g on s.id=g.id where gender='female';

# select s.name, s.id, s.gender, s.grade, g.grade from student s left join grades g on s.id=g.id where gender='male';

# select s.salesman_id, s.name, s.city, s.commission, c.customer_id, c.cust_name, c.city, c.grade, c.salesman_id from salesman s inner join customer c on s.city=c.city where city='New York';


