"""
实现函数 ToLowerCase()，该函数接收一个字符串参数 str，
并将该字符串中的大写字母转换成小写字母，之后返回新的字符串。

示例 1：
输入: "Hello"
输出: "hello"

示例 2：
输入: "here"
输出: "here"

示例 3：
输入: "LOVELY"
输出: "lovely"
"""

# 直接用内置函数:
# class Solution(object):
#     def toLowerCase(self, str):
#         """
#         :type str: str
#         :rtype: str
#         """
#         return str.lower()
# s = Solution()
# print(s.toLowerCase('Hello'))

# 具体的实现函数:
class Solution(object):
    def toLowerCase(self, str):
        """
        :type str: str
        :rtype: str
        """
        # ord函数可以将字符转化为你所需要的ASCII码
        for i in range(len(str)):
            if ord(str[i]) <= ord("Z") and ord(str[i]) >= ord("A"):
                str = str[:i] + chr(ord(str[i]) + (ord("a")- ord("A"))) + str[i+1:]
        return str
s = Solution()
print(s.toLowerCase('HeLlo'))