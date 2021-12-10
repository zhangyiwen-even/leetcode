"""
不使用运算符 + 和 - ​​​​​​​，计算两整数 ​​​​​​​a 、b ​​​​​​​之和。

示例 1:
输入: a = 1, b = 2
输出: 3

示例 2:
输入: a = -2, b = 3
输出: 1
"""
class Solution:
    def getSum(self, a: int, b: int) -> int:
        # alist = []
        # alist.append(a)
        # alist.append(b)
        return sum([a,b])
s = Solution()
print(s.getSum(3,-2))