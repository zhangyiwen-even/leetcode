"""
给定两个字符串 s 和 t，它们只包含小写字母。
字符串 t 由字符串 s 随机重排，然后在随机位置添加一个字母。
请找出在 t 中被添加的字母。

示例 1：
输入：s = "abcd", t = "abcde"
输出："e"
解释：'e' 是那个被添加的字母。

示例 2：
输入：s = "", t = "y"
输出："y"

示例 3：
输入：s = "a", t = "aa"
输出："a"

示例 4：
输入：s = "ae", t = "aea"
输出："a"
 
提示：
0 <= s.length <= 1000
t.length == s.length + 1
s 和 t 只包含小写字母
"""

# Counter是一个容器对象,主要的作用是用来统计散列对象,可以使用三种方式来初始化
# 参数里面参数可迭代对象 Counter("success")
# 传入关键字参数Counter((s=3,c=2,e=1,u=1))
# 传入字典 Counter({"s":3,"c"=2,"e"=1,"u"=1})
# Counter()对象还有几个可以调用的方法,代码里面分别进行了说明
# a.elements() # 获取a中所有的键,返回的是一个对象,我们可以通过list来转化它
# next函数next() 返回迭代器的下一个项目。 next() 函数要和生成迭代器的 iter() 函数一起使用。

# No.1
# from collections import Counter
# class Solution(object):
#     def findTheDifference(self, s, t):
#         """
#         :type s: str
#         :type t: str
#         :rtype: str
#         """
#         return next((Counter(t)-Counter(s)).elements())
# s = Solution()
# print(s.findTheDifference(s = "ae", t = "aea"))

# No.2
# class Solution(object):
#     def findTheDifference(self, s, t):
#         """
#         :type s: str
#         :type t: str
#         :rtype: str
#         """
#         num1 = 0
#         num2 = 0
#         for i in s:
#             num1 += ord(i)
#         for j in t:
#             num2 += ord(j)
#         return chr(num2 - num1)

# s = Solution()
# print(s.findTheDifference(s = "ae", t = "aea"))

# No.3
# from collections import Counter
# class Solution(object):
#     def findTheDifference(self, s, t):
#         """
#         :type s: str
#         :type t: str
#         :rtype: str
#         """
#         return ''.join((Counter(t)-Counter(s)).elements())
# s = Solution()
# print(s.findTheDifference(s = "abcd", t = "abcde"))
