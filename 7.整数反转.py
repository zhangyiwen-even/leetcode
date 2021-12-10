"""
题目描述：
给出一个 32 位的有符号整数，你需要将这个整数中每位上的数字进行反转。

示例 1:
输入: 123
输出: 321

示例 2:
输入: -123
输出: -321

示例 3:
输入: 120
输出: 21
注意:
假设我们的环境只能存储得下 32 位的有符号整数，则其数值范围为 [−2^31,  2^31 − 1]。
请根据这个假设，如果反转后整数溢出那么就返回 0。
"""

# 别人的答案
# class Solution(object):
#     def reverse(self, x):
#         a = str(x) if x>0 else str(-x)+'-'
#         a = int(a[::-1])
#         return a if a <= 2**31-1 and a >= -2**31-1 else 0
# s = Solution()
# print(s.reverse(1534236469))

# 自己的1，bug是不能判断越界的情况：
# class Solution(object):
#     def reverse(self, x):
#         """
#         :type x: int
#         :rtype: int
#         """
#         if x < 0:
#             a =  (-1) * int(str(abs(x))[::-1].lstrip('0'))
#             return int(str(a))
#         elif x > 0:
#             b = str(x)[::-1].lstrip('0')
#             return int(b)
#         else:
#             return 0
# s = Solution()
# print(s.reverse(1534236469))

# 修改后的，还是没有考虑好边界值：
# class Solution(object):
#     def reverse(self, x):
#         """
#         :type x: int
#         :rtype: int
#         """
#         if x == 0:
#             return 0
#         elif x < 0:
#             a =  (-1) * int(str(abs(x))[::-1].lstrip('0'))
#             return int(str(a))
#         elif x > 0:
#             b = str(x)
#             return int((b)[::-1].lstrip('0'))
#         elif  x < -2**31 or  x > (2**30)-1:
#             return 0
#         else:
#             return 0
# s = Solution()
# print(s.reverse(1534236469))

# 还是没有考虑好边界值：
# class Solution(object):
#     def reverse(self, x):
#         if x == 0:
#             return 0
#         elif x < 0 and x > -2**31:
#             a =  (-1) * int(str(abs(x))[::-1].lstrip('0'))
#             return int(str(a))
#         elif x > 0 and x < (2**30)-1:
#             b = str(x)
#             return int((b)[::-1].lstrip('0'))
#         else:
#             return 0
# s = Solution()
# print(s.reverse(1463847412))

# 别人答案：
class Solution(object):
    def reverse(self, x):
        # 第1种情况:
        if x == 0:
            return 0
        # 2
        # 转换为字符串    
        str_x = str(x)
        x = ''
        # 判断负数
        if str_x[0] == '-':
            x += '-'
        # 求反转结果  
        x += str_x[len(str_x)-1::-1].lstrip('0').rstrip("-")
        # str转换为int
        x = int(x)
        # 3 在此范围内的数执行第二步操作
        if -2**31 < x < 2**31-1:
            return x
        # 否则 输出0
        return 0
s = Solution()
print(s.reverse(1467412))    