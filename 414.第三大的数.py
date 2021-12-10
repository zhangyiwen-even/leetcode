"""
给定一个非空数组，返回此数组中第三大的数。如果不存在，则返回数组中最大的数。要求算法时间复杂度必须是O(n)。

示例 1:
输入: [3, 2, 1]
输出: 1
解释: 第三大的数是 1.

示例 2:
输入: [1, 2]
输出: 2
解释: 第三大的数不存在, 所以返回最大的数 2 .

示例 3:
输入: [2, 2, 3, 1]
输出: 1
解释: 注意，要求返回第三大的数，是指第三大且唯一出现的数。
存在两个值为2的数，它们都排第二。
"""
# 可以过 但是使用了sort函数不符合题目对于时间复杂度的要求:
# class Solution(object):
#     def thirdMax(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#         nums = list(set(nums))
#         # 长度小于3 返回最大的
#         if len(nums) < 3:
#             return max(nums)
#         # 否则 返回第三大的 sorted排序 取倒数第三个
#         return sorted(nums)[-3]
# s = Solution()
# print(s.thirdMax([1,2,-2147483648]))

class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = set(nums)
        if len(nums) < 3:
            return max(nums)
        nums.remove(max(nums))
        nums.remove(max(nums))
        return max(nums)
s = Solution()
print(s.thirdMax([1,2,-2147483648]))