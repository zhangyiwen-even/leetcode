"""
你是一个专业的小偷，计划偷窃沿街的房屋。每间房内都藏有一定的现金，影响你偷窃的唯一制约因素就是相邻的房屋装有相互连通的防盗系统，如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警。
给定一个代表每个房屋存放金额的非负整数数组，计算你 不触动警报装置的情况下 ，一夜之内能够偷窃到的最高金额。
 
示例 1：
输入：[1,2,3,1]
输出：4
解释：偷窃 1 号房屋 (金额 = 1) ，然后偷窃 3 号房屋 (金额 = 3)。
     偷窃到的最高金额 = 1 + 3 = 4 。

示例 2：
输入：[2,7,9,3,1]
输出：12
解释：偷窃 1 号房屋 (金额 = 2), 偷窃 3 号房屋 (金额 = 9)，接着偷窃 5 号房屋 (金额 = 1)。
     偷窃到的最高金额 = 2 + 9 + 1 = 12 。
 
提示：
0 <= nums.length <= 100
0 <= nums[i] <= 400
"""

# 思路有问题，测试用例过了1半 [2,1,1,2] 没过 正确输出应该是4 我的输出是3
# class Solution(object):
#     def rob(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#         # 计算所有索引是奇数/偶数的和，比较是奇数还是偶数的和是最大的，输出最大值
#         # 奇数
#         alist = []
#         # 偶数
#         blist = []
#         for i in range(0,len(nums),2):
#             alist.append(nums[i])
#         # return sum(alist)
#         return alist
#         # for j in range(1,len(nums),2):
#         #     blist.append(nums[j])
#         # return blist
#         # return max(sum(alist),sum(blist))
# s = Solution()
# print(s.rob([2,1,1,2]))

# 动态规划
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n == 0: return 0
        if n == 1: return nums[0]
        if n == 2: return max(nums[0],nums[1])

        dp = [0]*n
        dp[0] = nums[0]
        dp[1] = max(nums[0],nums[1])

        for i in range(2,n):
            dp[i] = max(dp[i-1],dp[i-2]+nums[i])
        return dp[-1]
s = Solution()
print(s.rob([2,1,1,2]))