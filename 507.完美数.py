"""
对于一个 正整数，如果它和除了它自身以外的所有 正因子 之和相等，我们称它为 「完美数」。
给定一个 整数 n， 如果是完美数，返回 true，否则返回 false

示例 1：
输入：28
输出：True
解释：28 = 1 + 2 + 4 + 7 + 14
1, 2, 4, 7, 和 14 是 28 的所有正因子。

示例 2：
输入：num = 6
输出：true

示例 3：
输入：num = 496
输出：true

示例 4：
输入：num = 8128
输出：true

示例 5：
输入：num = 2
输出：false
"""

# 结果是对的 但是超时了
# class Solution(object):
#     def checkPerfectNumber(self, num):
#         """
#         :type num: int
#         :rtype: bool
#         """
#         # 求所有因数，能整除的输到列表里
#         alist = []
#         for i in range(1,num):
#             if num % i == 0:
#                 alist.append(i)
#         # 判断正因子之和是否等于num
#         if sum(alist) == num:
#             return True
#         else:
#             return False
# s = Solution()
# print(s.checkPerfectNumber(2))

# 大佬们的算法 只有这6个数是幸福树
# class Solution(object):
#     def checkPerfectNumber(self, num):
#         """
#         :type num: int
#         :rtype: bool
#         """
#         # 只有列表里的是幸福数
#         alist = [6,28,496,8128,33550336]
#         if num in alist:
#             return True
#         else:
#             return False
# s = Solution()
# print(s.checkPerfectNumber(2))