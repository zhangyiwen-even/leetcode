"""
一个长度为n-1的递增排序数组中的所有数字都是唯一的，并且每个数字都在范围0～n-1之内。
在范围0～n-1内的n个数字中有且只有一个数字不在该数组中，请找出这个数字。

示例 1:
输入: [0,1,3]
输出: 2

示例 2:
输入: [0,1,2,3,4,5,6,7,9]
输出: 8
 
限制：
1 <= 数组长度 <= 10000
"""
# class Solution(object):
#     def missingNumber(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#         lens = len(nums)
#         res = lens
#         for i in range(0,lens):
#             tmp = nums[i] - i
#             res -= tmp
#         return res
# s = Solution()
# print(s.missingNumber([0,1,2,3,4,5,6,7,9]))

# 二分法
class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left,right = 0,len(nums)-1
        while left <= right:
            mid = (left+right) // 2
            if nums[mid] <= mid:
                left = mid + 1
            else:
                right = mid - 1
        return left
s = Solution()
print(s.missingNumber([1,2,3,4,5,6,7,8,9]))