"""
给定一个字符串，验证它是否是回文串，只考虑字母和数字字符，可以忽略字母的大小写。
说明：本题中，我们将空字符串定义为有效的回文串。
示例 1:
输入: "A man, a plan, a canal: Panama"
输出: true

示例 2:
输入: "race a car"
输出: false
"""

# 有问题，不能判断部分测试用例，比如0P
# import re,string
# class Solution(object):
#     def isPalindrome(self, s):
#         """
#         :type s: str
#         :rtype: bool
#         """
#         # 将字符串转换为小写,用replace函数，去除字符串中的空格
#         s = s.lower().replace(" ","")
#         # 去除字符串里的符号
#         punc = '~`!#$%^&*()_+-=|\';":/.,?><~·！@#￥%……&*（）——+-=“：’；、。，？》《{}'
#         s = re.sub(r"[%s]+" %punc,"",s)
#         if s == s[::-1]:
#             return True
#         else:
#             return False
#         # return s
# s = Solution()
# print(s.isPalindrome(".,"))

# ac的答案：
# class Solution(object):
#     def isPalindrome(self, s):
#         """
#         :type s: str
#         :rtype: bool
#         """
#         a = ''.join(filter(str.isalnum,s)).lower()
#         return a == a[::-1]
# s = Solution()
# print(s.isPalindrome("A man, a plan, a canal: Panama"))

# # 正则表达式求解: 
# import re
# class Solution(object):
#     def isPalindrome(self, s):
#         """
#         :type s: str
#         :rtype: bool
#         """
#         s = re.sub('[^a-zA-Z0-9]','',s)
#         s = s.lower()
#         return s==s[::-1]
# s = Solution()
# print(s.isPalindrome('0P'))