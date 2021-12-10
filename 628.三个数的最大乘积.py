"""
给定一个整型数组，在数组中找出由三个数组成的最大乘积，并输出这个乘积。

示例 1:
输入: [1,2,3]
输出: 6

示例 2:
输入: [1,2,3,4]
输出: 24

注意:
给定的整型数组长度范围是[3,104]，数组中所有的元素范围是[-1000, 1000]。
输入的数组中任意三个数的乘积不会超出32位有符号整数的范围。
"""

# [-4,-3,1,2] or [-4,3,1,2] or [1,2,3,4]
# 思路: 先将列表排序，
# 如果全为正数，那么最后的3个数乘积为最大，
# 如果有负数，要么是最后三个正数乘积最大，要么是前两个负数与最后一个正数乘积为最大
class Solution(object):
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = sorted(nums)
        return max(nums[-1]*nums[-2]*nums[-3],nums[0]*nums[1]*nums[-1])
s = Solution()
print(s.maximumProduct([4,3,2,1]))