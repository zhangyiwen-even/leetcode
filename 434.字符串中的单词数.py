"""
统计字符串中的单词个数，这里的单词指的是连续的不是空格的字符。
请注意，你可以假定字符串里不包括任何不可打印的字符。

示例:
输入: "Hello, my name is John"
输出: 5
解释: 这里的单词是指连续的不是空格的字符，所以 "Hello," 算作 1 个单词。
"""
# class Solution(object):
#     def countSegments(self, s):
#         """
#         :type s: str
#         :rtype: int
#         """
#         str_a = s.split()
#         return len(str_a)
# s = Solution()
# print(s.countSegments("Hello, my name is John"))

# 正则表达式的解法:
import re
class Solution(object):
    def countSegments(self, s):
        """
        :type s: str
        :rtype: int
        """
        return len(re.findall('[^\s]+',s))
s = Solution()
print(s.countSegments("Hello, i my name is John"))