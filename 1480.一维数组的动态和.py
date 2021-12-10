"""
给你一个数组 nums 。数组「动态和」的计算公式为：runningSum[i] = sum(nums[0]…nums[i]) 。
请返回 nums 的动态和。

示例 1：
输入：nums = [1,2,3,4]
输出：[1,3,6,10]
解释：动态和计算过程为 [1, 1+2, 1+2+3, 1+2+3+4] 。

示例 2：
输入：nums = [1,1,1,1,1]
输出：[1,2,3,4,5]
解释：动态和计算过程为 [1, 1+1, 1+1+1, 1+1+1+1, 1+1+1+1+1] 。

示例 3：
输入：nums = [3,1,2,10,1]
输出：[3,4,6,16,17]

提示：
1 <= nums.length <= 1000
-10^6 <= nums[i] <= 10^6
"""

# No.1
# class Solution(object):
#     def runningSum(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: List[int]
#         """
#         for i in range(1,len(nums)):
#             nums[i] = nums[i] + nums[i-1]
#         return nums
# s = Solution()
# print(s.runningSum([1,2,3,4]))

# No.2
# class Solution(object):
#     def runningSum(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: List[int]
#         """
#         return [sum(nums[0:i+1]) for i in range(len(nums))]
# s = Solution()
# print(s.runningSum([1,2,3,4]))

# No.3
class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # 新定义一个列表
        alist = []
        # 加入列表中的元素，是累加的结果
        sum = 0
        for i in nums:
            sum += i
            alist.append(sum)
        return alist
s = Solution()
print(s.runningSum([1,2,3,4,5,6]))