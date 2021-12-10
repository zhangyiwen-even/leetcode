"""
题目描述：
给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。
你可以假设每种输入只会对应一个答案。但是，数组中同一个元素不能使用两遍。
示例:

给定 nums = [2, 7, 11, 15], target = 9

因为 nums[0] + nums[1] = 2 + 7 = 9
所以返回 [0, 1]
"""

# class Solution(object):
#     def twoSum(self, nums, target):
#         """
#         :type nums: List[int]
#         :type target: int
#         :rtype: List[int]
#         """
#         # 从第一个元素开始遍历:
#         for i in range(len(nums)):
#             # 从第二个元素开始遍历:
#             for j in range(i+1,len(nums)):
#                 # 根据索引取列表元素的值
#                 if nums[i] + nums[j] == target:
#                     # 返回索引
#                     return [i,j]
# s = Solution()
# print(s.twoSum([11, 7, 2, 15],9))

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            for j in range(i,len(nums)):
                if nums[i] + nums[j] == target:
                    return [i,j]
s = Solution()
print(s.twoSum([2,7,11,15],9))