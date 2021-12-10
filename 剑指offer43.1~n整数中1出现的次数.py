"""
输入一个整数 n ，求1～n这n个整数的十进制表示中1出现的次数。
例如，输入12，1～12这些整数中包含1 的数字有1、10、11和12，1一共出现了5次。

示例 1：
输入：n = 12
输出：5

示例 2：
输入：n = 13
输出：6
限制：
1 <= n < 2^31
"""

# 结果在本地测试是正确的，但是提交会报错memory error.
# class Solution(object):
#     def countDigitOne(self, n):
#         """
#         :type n: int
#         :rtype: int
#         """
#         alist = []
#         for i in range(1,n+1):
#             for j in str(i):
#                 alist.append(int(j))
#         return alist.count(1)

# s = Solution()
# print(s.countDigitOne(13))     

# 转化成字符串的方式也会超时，memory error
# class Solution(object):
#     def countDigitOne(self, n):
#         """
#         :type n: int
#         :rtype: int
#         """
#         numstr = ''
#         for num in range(1,n+1):
#             numstr += str(num)
#         # return numstr
#         return numstr.count('1')
# s = Solution()
# print(s.countDigitOne(12))     


# ac的答案：
# class Solution(object):
#     def countDigitOne(self, n):
#         """
#         :type n: int
#         :rtype: int
#         """
#         ans = 0
#         t = 1
#         for i in range(len(str(n))-1,0,-1):
#             num = 10*i
#             a = n // num
#             if a > t:
#                 ans += num
#             elif a == t:
#                 ans += n - num + 1
#             while n > num:
#                 ans += i * num // 10
#                 n -= num
#         return ans+(n>=t)
# s = Solution()
# print(s.countDigitOne(12))