"""
一只青蛙一次可以跳上1级台阶，也可以跳上2级台阶。求该青蛙跳上一个 n 级的台阶总共有多少种跳法。
答案需要取模 1e9+7（1000000007），如计算初始结果为：1000000008，请返回 1。

示例 1：
输入：n = 2
输出：2

示例 2：
输入：n = 7
输出：21

示例 3：
输入：n = 0
输出：1

提示：
0 <= n <= 100
"""
# 剑指offer的方法
# class Solution(object):
#     def numWays(self, n):
#         """
#         :type n: int
#         :rtype: int
#         """
#         if n == 0:
#             return 1
#         a = 1
#         b = 1
#         for i in range(n):
#             a,b = b,a+b
#         return a % 1000000007
# s = Solution()
# print(s.numWays(8))