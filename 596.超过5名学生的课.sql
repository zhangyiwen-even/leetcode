"""
有一个courses 表 ，有: student (学生) 和 class (课程)。
请列出所有超过或等于5名学生的课。

例如，表：
+---------+------------+
| student | class      |
+---------+------------+
| A       | Math       |
| B       | English    |
| C       | Math       |
| D       | Biology    |
| E       | Math       |
| F       | Computer   |
| G       | Math       |
| H       | Math       |
| I       | Math       |
+---------+------------+

应该输出:
+---------+
| class   |
+---------+
| Math    |
+---------+
 
提示：
学生在每个课中不应被重复计算。
"""

-- select class from cources  WHERE COUNT(class) > 5;
SELECT class FROM courses GROUP BY class HAVING count(distinct student) >= 5 