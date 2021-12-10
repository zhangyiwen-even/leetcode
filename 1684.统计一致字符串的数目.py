"""
给你一个由不同字符组成的字符串 allowed 和一个字符串数组 words 。如果一个字符串的每一个字符都在 allowed 中，就称这个字符串是 一致字符串 。
请你返回 words 数组中 一致字符串 的数目。

示例 1：
输入：allowed = "ab", words = ["ad","bd","aaab","baa","badab"]
输出：2
解释：字符串 "aaab" 和 "baa" 都是一致字符串，因为它们只包含字符 'a' 和 'b' 。

示例 2：
输入：allowed = "abc", words = ["a","b","c","ab","ac","bc","abc"]
输出：7
解释：所有字符串都是一致的。

示例 3：
输入：allowed = "cad", words = ["cc","acd","b","ba","bac","bad","ac","d"]
输出：4
解释：字符串 "cc"，"acd"，"ac" 和 "d" 是一致字符串。

提示：
1 <= words.length <= 104
1 <= allowed.length <= 26
1 <= words[i].length <= 10
allowed 中的字符 互不相同 。
words[i] 和 allowed 只包含小写英文字母。
"""

# 看一下python版本。小于等于是子集的意思。为true则记为1，false为0。
# class Solution(object):
#     def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
#         """
#         :type allowed: str
#         :type words: List[str]
#         :rtype: int
#         """
#         return sum([set(word) <= set(allowed) for word in words])
# s = Solution()
# print(s.countConsistentStrings(allowed = "ab", words = ["ad","bd","aaab","baa","badab"]))


class Solution(object):
    def countConsistentStrings(self, allowed, words):
        count = 0
        for i in words:
            lens = len(i)
            for j in i:
                if j in allowed:
                    lens -= 1
            if lens == 0:
                count += 1
        return count
s = Solution()
print(s.countConsistentStrings(allowed = "ab", words = ["ad","bd","aaab","baa","badab"]))