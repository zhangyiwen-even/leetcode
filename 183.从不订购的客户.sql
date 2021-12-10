"""
某网站包含两个表，Customers 表和 Orders 表。编写一个 SQL 查询，找出所有从不订购任何东西的客户。

Customers 表：
+----+-------+
| Id | Name  |
+----+-------+
| 1  | Joe   |
| 2  | Henry |
| 3  | Sam   |
| 4  | Max   |
+----+-------+

Orders 表：
+----+------------+
| Id | CustomerId |
+----+------------+
| 1  | 3          |
| 2  | 1          |
+----+------------+

例如给定上述表格，你的查询应返回：
+-----------+
| Customers |
+-----------+
| Henry     |
| Max       |
+-----------+
"""
1.左连接
SELECT Name AS Customers FROM Customers left Join Orders ON Customers.Id = Orders.CustomerId WHERE Orders.CustomersId is NULL;

解释
select * from tab1 where not exists (select 1 from tab2 where tab1.col=tab2.col)
看这个条件tab1.col=tab2.col，如果存在这样的数据子查询就返回1.
整个查询的意思就是在tab1中存在，在tab2中不存在的数据
把tab1中所有与tab2的col对应列值相同的记录去除以后的所有记录
select 1 from 就是说不关心具体的记录，只关心是否有结果。

2.
SELECT NAME AS Customers FROM Customers WHERE NOT EXISTS (SELECT 1 FROM Orders WHERE Orders.CustomersId = Customers.Id);

3.
SELECT NAME AS Customers FROM Customers WHERE Customers.Id not in (SELECT distinct Orders.CustomersId FROM Orders);