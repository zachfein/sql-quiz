PROBLEMS = [
{   # Problem 1 -- a basic select
"instruction":
"""The 'select' is the basic query. We use it to extract information from a
table. There are a number of clauses to a select statement. Right now, we'll
concern ourself with just two: the column list and the table you are querying.
The format of the basic select statement is

    SELECT <column list> FROM <table name>;

For now, we can use the wildcard '*' (without quotes) to select all columns
from a given table.

Examples: http://sqlzoo.net/wiki/SELECT_from_WORLD_Tutorial -- 1""",

"task":
"""Write a query that shows all the information about all the salespeople in
the database. Use a basic SELECT query.""",

"hint": """Select all the columns from the 'salespeople' table.""",

"solution": """SELECT * FROM salespeople;"""
},

{   # Problem 2 -- select with a where clause
"instruction":
"""Select statements can have an additional clause called the 'where' clause.
This lets us extract specific rows out of our table. Our where clause can be
specific enough to match a single row, or general enough to match a set of
rows. The format of a select statement with a 'where' clause is:

    SELECT <column list> FROM <table name> WHERE <equality expression>;

Examples: http://sqlzoo.net/wiki/SELECT_basics -- 1""",

"task":
"""Write a query that shows all the information about all salespeople from
the 'Northwest' region.""",

"hint": """Select all the columns from the 'salespeople' table where the region
matches the string 'Northwest'.""",

"solution": """SELECT * FROM salespeople WHERE region = 'Northwest';""",
},

{   # Problem 3 -- select individual columns
"instruction":
"""We've been selecting all the columns out of our table up until now, but the
amount of data can be overwhelming. We can use the column list to specify
individual columns. We do this by specifying the column list as a single column
name instead of a '*'.

Examples: http://sqlzoo.net/wiki/SELECT_from_WORLD_Tutorial -- 1""",

"task": """Write a query that shows just the emails of the salespeople from the
'Southwest' region.""",

"hint":
"""Select the email column from the 'salespeople' table where the
region matches the string 'Southwest'.""",

"solution":  """SELECT email FROM salespeople WHERE region = 'Southwest';"""
},

{   # Problem 4 -- select more than one column
"instruction":
"""We can ask for more than one column from the data set by specifying all the
columns separated by commas.

Examples: http://sqlzoo.net/wiki/SELECT_from_Nobel_Tutorial -- 1, 2
          http://sqlzoo.net/wiki/SELECT_from_WORLD_Tutorial -- 1""",

"task": """Write a query that shows the first name, last name, and email of all
salespeople in the 'Northwest' region.""",

"hint": """Select the first name, last name, and email column from the
'salespeople' table where the region matches the string 'Northwest'.""",

"solution": """SELECT first_name, last_name, email FROM salespeople WHERE region = 'Northwest';"""
},

{   # Problem 5 -- inequality query
"instruction":
"""In addition to finding exact matches, we can specify the where clause of our
query to match a range of columns using inequalities.

Examples: http://sqlzoo.net/wiki/SELECT_basics -- 2, 3
          http://sqlzoo.net/wiki/SELECT_from_WORLD_Tutorial -- 2""",

"task": """Write a query that shows the common name of melons that cost more than
$5.00.""",

"hint": """Select the common_name column from the 'melons' table where the
price column is greater than 5.0.""",

"solution": """SELECT common_name FROM melons WHERE price > 5.0;"""
},

{   # Problem 6 -- and clause
"instruction":
"""Sometimes, we want to filter down our matched rows even further. We can add
additional restrictions to our query using an 'and' clause. It looks like this:

    SELECT <column list> FROM <table> WHERE <expression 1> AND <expression 2>;

Examples: http://sqlzoo.net/wiki/SELECT_basics -- 3, 6""",

"task": """Write a query that shows the common name and price for all
watermelons that cost more than $5.00.
""",
"hint": """Select the common_name and price columns from the 'melons'
table where the price is greater than 5.0 and the melon_type is
'Watermelon'. """,
"solution": """SELECT common_name, price FROM melons WHERE price > 5.0 AND melon_type = 'Watermelon';"""
},

{   # Problem 7 -- like clause, simple wildcard
"instruction":
"""Using inequalities on numeric columns lets us match a range of rows.
Similarly, we can use a string wildcard to do matches on ranges of strings.
Confusingly, the string wildcard is '%', which is different from the column
wildcard, which is '*'. Additionally, you can't use an equality to match a
string wildcard, you have to use a 'like' clause instead. The format is as
follows:

    <column_name> LIKE '<match string with wildcards>'

Examples: http://sqlzoo.net/wiki/SELECT_basics -- 5""",

"task": """Write a query that displays all common names of melons that start with
the letter 'C'.
""",

"hint": """Select the common_name column from the 'melons' table where the
common name is like the letter 'C' followed by a wildcard.""",

"solution": """SELECT common_name FROM melons WHERE common_name LIKE 'C%';"""
},

{   # Problem 8 -- more complex wildcard
"instruction":
"""String wildcards can be places anywhere in a string, allowing you to match
complex patterns. For example, the string pattern 'W%termelon%' matches the
strings 'Watermelon', 'Wintermelon', 'Watermelons', and 'Wintermelons'.

Examples: http://sqlzoo.net/wiki/SELECT_basics -- 5""",

"task": """Write a query that shows the common name of any melon with 'Golden'
anywhere in the common name.
""",

"hint": """Select the common_name column from the 'melons' table where the
common name is like the word 'Golden', surrounded on either side by a
wildcard.""",

"solution": """SELECT common_name FROM melons WHERE common_name LIKE '%Golden%';"""
},

{   # Problem 9 -- distinct keyword
"instruction":
"""Frequently, you will encounter duplicate data across multiple rows. In our
salespeople table schema, we can see that each one is attached to a specific
'region'. If we query that table for all the different regions that are used,
sql will return duplicates, one for each salesperson in our table.
To counter this, we can use the 'distinct' keyword. In our column list, we can
prepend the keyword to the column name.

Examples: http://sqlzoo.net/wiki/Using_SUM,_Count,_MAX,_DISTINCT_and_ORDER_BY -- 2
          http://sqlzoo.net/wiki/SUM_and_COUNT -- 2""",

"task": """Write a query that shows all the distinct regions that a salesperson can belong to.
""",

"hint": """Select the distinct entries in the region column from the 'salespeople' table. """,

"solution": """SELECT DISTINCT region FROM salespeople;"""
},

{   # Problem 10 -- 'or' clause
"instruction":
"""Earlier, we used the 'and' keyword to narrow down our query: we made our
search more specific. We can use the 'or' keyword in exactly the opposite way,
to make our search match more rows.
Example: http://sqlzoo.net/wiki/SELECT_basics -- 6""",

"task": """Write a query that shows the emails of all salespeople from both the
Northwest and Southwest regions.
""",

"hint": """Select the email column from the 'salespeople' table where the
region is either 'Northwest' or 'Southwest'. Use the 'or' clause to do
that.""",

"solution": """SELECT email FROM salespeople WHERE region = 'Northwest' OR region = 'Southwest';"""
},

{   # Problem 11 -- 'in' clause
"instruction":
"""It can be tedious to match a single column against multiple options. In our
previous exercise, we searched for the region to match both 'Northwest' and
'Southwest'. If we had more options we were trying to match, this would make
our query very long. We can use an 'in' clause to write this kind of query more
succinctly. We can replaces a series of 'or' clauses with a single 'in' clause
that takes the following format:

    <column name> IN (<option1>, <option2>, <...>)

Example: http://sqlzoo.net/wiki/SELECT_basics -- 4""",

"task": """Write a query that shows the emails of all salespeople from both the
Northwest and Southwest regions, this time using an 'IN' clause.
""",

"hint": """Select the email column from the 'salespeople' table where the
region is in the list of 'Northwest' and 'Southwest'. Use the 'in' clause.""",

"solution": """SELECT email FROM salespeople WHERE region IN ('Northwest', 'Southwest');"""
},

{   # Problem 12 -- combining column selection, in clause, and wildcards
"instruction":
"""Using all these tools, we can bring them together to do fairly complex
queries that match many different rows. Using what you've learned, write a
query that combines column selection, an 'in' clause, and string wildcards.""",

"task": """Write a query that shows the email, first name, and last name of all
salespeople in either the Northwest or Southwest regions whose last names start
with the letter 'M'.""",

"hint": """Select the email, first_name, and last_nme columns from the
'salespeople' table where the region is in the list of 'Northwest', and
'Southwest', and where the last_name matches the character 'M' followed by a
wildcard.""",

"solution": """SELECT email, first_name, last_name FROM salespeople WHERE region IN ('Northwest', 'Southwest') AND last_name LIKE 'M%';"""
},

{   # Problem 13 -- computed columns
    # Show the price in euros
"instruction": """An odd feature of sql is the ability to select data out of a
table that doesn't actually exist. Certain kinds of data can be computed on the
fly and be made to look as if they were part of the table. We'll use this to
query for melon price in USD and EUR, where one column will be computed from
the other.

Examples: http://sqlzoo.net/wiki/SELECT_basics -- 2""",

"task": """Write a query that shows the melon type, common name, price, and the
price of the melon given in euros. The 'melons' table has prices in dollars,
and the dollar to euro conversion rate is 0.73.
""",

"hint": """Select the melon_type, common_name, price, and a computed column
which is the price multiplied by the value .73 from the table 'melons'.""",

"solution": """SELECT melon_type, common_name, price, price*.73 FROM melons;"""
},

{   # Problem 14 -- aggregate functions, count
    #-> How many customers do we have?
"instruction":

"""Similar to the 'computed' columns, SQL has a set of predefined 'aggregate'
functions that operate on an entire set of matched rows. Aggregate functions
condense a set of rows into a single row. An example of this kind of aggregate
operation is a 'count'. It simply counts up all the matched rows and returns a
single record in their place.

Example: http://sqlzoo.net/wiki/The_nobel_table_can_be_used_to_practice_more_SUM_and_COUNT_functions. -- 1""",

"task": """Write a query that shows the total number of customers in our customer
table.""",

"hint": """Select the count of all the columns from the table 'customers'. """,

"solution": """SELECT count(*) FROM customers;"""
},

{   # Problem 15 -- aggregate functions with where clauses
# -> How many orders were shipped to California?
"instruction":
"""We can combine aggregate functions with the standard SQL clauses we've seen
so far. In this exercise, you will combine a count clause with a where clause
to limit what is counted.""",

"task": """Write a query that counts the number of orders (in the orders table) shipped to California.""",

"hint": """Select the count of all the columns from the table 'orders' where
the shipto_state is 'CA'.""",

"solution": """SELECT count(*) FROM orders WHERE shipto_state = 'CA';"""
},

{   # Problem 16 -- sum function
    # -> dollar total for all orders
"instruction":
"""Aggregate functions work on column lists. When we're counting things, it
doesn't matter which column we count, there should be the same number of each
column across all the records. For this reason, it is customary to execute the
count on all the columns in the query. With other aggregate functions, the
column we use can be meaningful, for example, if we are totaling up the values
in a single column.

Examples: http://sqlzoo.net/wiki/SUM_and_COUNT -- 1
          http://sqlzoo.net/wiki/The_nobel_table_can_be_used_to_practice_more_SUM_and_COUNT_functions. -- 3""",

"task": """Write a query that shows the total amount of money spent across all melon
orders.""",

"hint": """Select the sum of the order_total column from the table 'orders'.""",

"solution": """SELECT SUM(order_total) FROM orders;"""
},

{   # Problem 17 -- avg function
    #-> What is the average order amount?
"instruction":
"""Another useful aggregate function is the average.""",

"task": """Write a query that shows the average order cost.""",

"hint": """Select the average of the order_total from the table 'orders'.""",

"solution": """SELECT AVG(order_total) FROM orders;"""
},

{   # Problem 18 -- min function
    # - -> What is the smallest (dollar amount) order?
"instruction":
"""Lastly, we have aggregate functions to select both the minimum or maximum values
of a column.""",

"task": """Write a query that shows the order total that was lowest in price.""",

"hint": """Select the minimum of the order_total from the table 'orders'. """,

"solution": """SELECT MIN(order_total) FROM orders;"""
},

{   # Problem 19 -- english query
"instruction":
"""Now, for a change of pace, we're going to try to write queries that can
show us information that spans multiple tables. Before we can do that though,
a quick review.""",

"task": """Write a query that fetches the id of the customer whose email is
'pclark74@gmail.com'.""",

"hint": """Select the id column from the 'customers' table where the email matches the string 'pclark74@gmail.com'""",

"solution": """SELECT id FROM customers WHERE email = 'pclark74@gmail.com';"""
},

{   # Problem 20 -- english query 2
"instruction":
"""We've identified Phyllis in our previous exercise to be customer number 100.""",

"task": """Write a query that shows the id, status and order_total for all orders
made by customer 100.""",

"hint": """Select the id, status, and order_total columns from the `orders` table where the customer id is 100.""",

"solution": """SELECT id, status, order_total FROM orders WHERE customer_id = 100;"""
},

{   # Problem 21 -- select-within-a-select
    #-> Get the orders for Phyliss by email address
"instruction":
"""One technique for writing queries that cross tables is using a subselect.
It lets us use the results of a query in the where clause of another query. In
this case, we can query the 'orders' table for orders matching the 'id' that
comes out of a different query. This lets us combine the previous two
queries into a single query.

Examples: http://sqlzoo.net/wiki/SELECT_within_SELECT_Tutorial -- 1""",

"task": """Write a single query that shows the id, status, and order total for all
orders made by 'pclark74@gmail.com'. Use a subselect to do this.
""",

"hint": """Select the id, status, and order_total columns from the 'orders'
table where the customer id matches the result from a subselect that queries
for the id column from the 'customers' table where the email matches the string
'pclark74@gmail.com'.""",

"solution": """SELECT id, status, order_total FROM orders WHERE customer_id = (SELECT id FROM customers WHERE email = 'pclark74@gmail.com');"""
},

{   # Problem 22 -- The null keyword
    # -> Get total amount of web orders (no sales person id)
"instruction":
"""In our system, an order can be attached to a salesperson in order to give
them commission. However, some orders come in from the web, which means some
orders have no salesperson. This is indicated in our table by having the
salesperson id be 'NULL', similar to python's 'None'.""",

"task": """Write a query that shows the total amount of revenue that comes from
internet orders.""",

"hint": """Select the sum of the order_total column from the 'orders' table
where the salesperson_id is null.""",

"solution": """SELECT SUM(order_total) FROM orders WHERE salesperson_id IS NULL;"""
}
]