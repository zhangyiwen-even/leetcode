"""
给你一个数组 nums ，数组中有 2n 个元素，按 [x1,x2,...,xn,y1,y2,...,yn] 的格式排列。
请你将数组按 [x1,y1,x2,y2,...,xn,yn] 格式重新排列，返回重排后的数组。

示例 1：
输入：nums = [2,5,1,3,4,7], n = 3
输出：[2,3,5,4,1,7] 
解释：由于 x1=2, x2=5, x3=1, y1=3, y2=4, y3=7 ，所以答案为 [2,3,5,4,1,7]

示例 2：
输入：nums = [1,2,3,4,4,3,2,1], n = 4
输出：[1,4,2,3,3,2,4,1]

示例 3：
输入：nums = [1,1,2,2], n = 2
输出：[1,2,1,2]

提示：
1 <= n <= 500
nums.length == 2n
1 <= nums[i] <= 10^3
"""
# No.1 重新赋值，利用python的简洁性。
# class Solution(object):
#     def shuffle(self, nums, n):
#         """
#         :type nums: List[int]
#         :type n: int
#         :rtype: List[int]
#         """
#         # 重新赋值: [::2]表示从0开始,以2为步长,[1::2]表示从1开始,2位步长,
#         # [:n]表示第n个数之前的元素,[n:]表示第n个之后的元素。
#         nums[::2],nums[1::2] = nums[:n],nums[n:]
#         return nums
# s = Solution()
# print(s.shuffle([1,2,3,4,4,3,2,1],4))
        
# No.2 
class Solution(object):
    def shuffle(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: List[int]
        """
        alist = []
        j = n
        for i in range(len(nums)-n):
            alist.append(nums[i])
            alist.append(nums[j])
            j += 1
        return alist
s = Solution()
print(s.shuffle([1,2,3,4,4,3,2,1],4))