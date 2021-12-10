"""
某城市开了一家新的电影院，吸引了很多人过来看电影。该电影院特别注意用户体验，专门有个 LED显示板做电影推荐，
上面公布着影评和相关电影描述。
作为该电影院的信息部主管，您需要编写一个 SQL查询，找出所有影片描述为非 boring (不无聊) 的并且 id 为奇数 的影片，
结果请按等级 rating 排列。

例如，下表 cinema:
+---------+-----------+--------------+-----------+
|   id    | movie     |  description |  rating   |
+---------+-----------+--------------+-----------+
|   1     | War       |   great 3D   |   8.9     |
|   2     | Science   |   fiction    |   8.5     |
|   3     | irish     |   boring     |   6.2     |
|   4     | Ice song  |   Fantacy    |   8.6     |
|   5     | House card|   Interesting|   9.1     |
+---------+-----------+--------------+-----------+
对于上面的例子，则正确的输出是为：
+---------+-----------+--------------+-----------+
|   id    | movie     |  description |  rating   |
+---------+-----------+--------------+-----------+
|   5     | House card|   Interesting|   9.1     |
|   1     | War       |   great 3D   |   8.9     |
+---------+-----------+--------------+-----------+
"""
"""
sql 中 & 是且的意思
<> 是 不等于 的意思
order by 是根据指定的列对结果集进行排序，默认是对结果进行升序排序
最大值的位置: 如果是ASC升序则排最后，DESC降序则排最前
"""

SELECT id,movie,description,rating from cinema where id & 1 and description <> 'boring' order by rating DESC 

SELECT id,movie,description,rating from cinema where description != 'boring' and id % 2 = 1 order by rating DESC