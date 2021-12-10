"""
设计一个函数把两个数字相加。不得使用 + 或者其他算术运算符。

示例:
输入: a = 1, b = 1
输出: 2

提示：
a, b 均可能是负数或 0
结果不会溢出 32 位整数
"""

# No.1
# class Solution(object):
#     def add(self, a, b):
#         """
#         :type a: int
#         :type b: int
#         :rtype: int
#         """
#         return sum([a,b])
# s = Solution()
# print(s.add(1,1))

# No.2
# import numpy as np
# class Solution(object):
#     def add(self, a, b):
#         """
#         :type a: int
#         :type b: int
#         :rtype: int
#         """
#         return int(np.sum((a,b)))
# s = Solution()
# print(s.add(1,1))

# No.3
class Solution(object):
    def add(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        mask = 0xffffffff
        while b:
            a,b = (a^b) & mask,((a&b) << 1) & mask
        return a if a < 0x80000000 else ~(a ^ mask)
s = Solution()
print(s.add(1,3))