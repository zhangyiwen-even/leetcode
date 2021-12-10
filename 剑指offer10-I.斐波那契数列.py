"""
写一个函数，输入 n ，求斐波那契（Fibonacci）数列的第 n 项。斐波那契数列的定义如下：
F(0) = 0,   F(1) = 1
F(N) = F(N - 1) + F(N - 2), 其中 N > 1.
斐波那契数列由 0 和 1 开始，之后的斐波那契数就是由之前的两数相加而得出。
答案需要取模 1e9+7（1000000007），如计算初始结果为：1000000008，请返回 1。
示例 1：
输入：n = 2
输出：1

示例 2：
输入：n = 5
输出：5

提示：
0 <= n <= 100
"""

# 递归会超时，这里用动态规划求解
# class Solution(object):
#     def fib(self, n):
#         """
#         :type n: int
#         :rtype: int
#         """
#         if n == 0:
#             return 0
#         elif n == 1:
#             return 1
#         else:
#             a = 0
#             b = 1
#             while n > 1 and n <= 100:
#                 a,b = b,a+b
#                 n -= 1
#             # 取模
#             return b%1000000007
# s = Solution()
# print(s.fib(5))

# lru_cache 缓存装饰器
# from functools import lru_cache
# class Solution(object):
#     @lru_cache(None)
#     def fib(self,n:int) -> int:
#         if n < 2:
#             return n
#         return (self.fib(n-1)+self.fib(n-2))%1000000007
# s = Solution()
# print(s.fib(10))

