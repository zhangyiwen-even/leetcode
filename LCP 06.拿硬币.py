"""
桌上有 n 堆力扣币，每堆的数量保存在数组 coins 中。我们每次可以选择任意一堆，拿走其中的一枚或者两枚，求拿完所有力扣币的最少次数。

示例 1：
输入：[4,2,1]
输出：4
解释：第一堆力扣币最少需要拿 2 次，第二堆最少需要拿 1 次，第三堆最少需要拿 1 次，总共 4 次即可拿完。

示例 2：
输入：[2,3,10]
输出：8

限制：
1 <= n <= 4
1 <= coins[i] <= 10
"""
# / : 比如1/2=0.5，所以需要四舍五入取整
# 向上取整的办法:
# 向上取整需要用到 math 模块中的 ceil() 方法:
# >>> import math
# >>> math.ceil(3.25)
# 4.0

import math
class Solution(object):
    def minCount(self, coins):
        """
        :type coins: List[int]
        :rtype: int
        """
        alist = []
        for i in coins:
            # i = i / 2
            # 对i取整,将i的值插入列表
            alist.append(math.ceil(i/2))
        return sum(alist)
s = Solution()
print(s.minCount([4,2,1]))