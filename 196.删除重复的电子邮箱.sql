"""
编写一个 SQL 查询，来删除 Person 表中所有重复的电子邮箱，重复的邮箱里只保留 Id 最小 的那个。
+----+------------------+
| Id | Email            |
+----+------------------+
| 1  | john@example.com |
| 2  | bob@example.com  |
| 3  | john@example.com |
+----+------------------+

Id 是这个表的主键。
例如，在运行你的查询语句之后，上面的 Person 表应返回以下几行:
+----+------------------+
| Id | Email            |
+----+------------------+
| 1  | john@example.com |
| 2  | bob@example.com  |
+----+------------------+
 
提示：
执行 SQL 之后，输出是整个 Person 表。
使用 delete 语句。
"""
-- SELECT DISTINCT Email FROM Person;

DELETE p1 FROM Person AS p1 JOIN Person AS p2 ON p1.id > p2.id AND p1.Email = p2.Email;

DELETE FROM Person WHERE id NOT IN (select Id FROM(SELECT MIN(id) as id FROM Person Group by Email) t );

DELETE p1 FROM Person AS p1,Person AS p2 WHERE p1.id > p2.id AND p1.Email = p2.Email;
