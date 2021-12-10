"""
编写一个 SQL 查询，获取 Employee 表中第二高的薪水（Salary） 。
+----+--------+
| Id | Salary |
+----+--------+
| 1  | 100    |
| 2  | 200    |
| 3  | 300    |
+----+--------+

例如上述 Employee 表，SQL查询应该返回 200 作为第二高的薪水。如果不存在第二高的薪水，那么查询应返回 null。
+---------------------+
| SecondHighestSalary |
+---------------------+
| 200                 |
+---------------------+
"""

-- SELECT First Salary AS SecondHighestSalary FROM Employee ORDER BY Salary DESC

-- No.1 子链接:
SELECT max(Salary) AS SecondHighestSalary FROM Employee WHERE Salary < (SELECT max(Salary) FROM Employee);

-- No.2 窗口函数:
SELECT max(Salary) AS SecondHighestSalary FROM (SELECT Salary,DENSE_RANK() OVER (ORDER BY Salary DESC) as rank_num
      FROM Employee
    )
WHERE rank_num = 2;


-- No.3 ifnull:
-- distinct 过滤关键字
-- ifnull(x,y), 若不为空则返回x，否则返回y，这道题y=null
-- limit x,y, 找到对应的记录就停止

SELECT ifnull(
    (SELECT DISTINCT Salary FROM Employee order by Salary DESC limit 1,1),NULL
)as 'SecondHighestSalary';


