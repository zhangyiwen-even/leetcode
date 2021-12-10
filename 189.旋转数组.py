"""
给定一个数组，将数组中的元素向右移动 k 个位置，其中 k 是非负数。

示例 1:
输入: [1,2,3,4,5,6,7] 和 k = 3
输出: [5,6,7,1,2,3,4]
解释:
向右旋转 1 步: [7,1,2,3,4,5,6]
向右旋转 2 步: [6,7,1,2,3,4,5]
向右旋转 3 步: [5,6,7,1,2,3,4]

示例 2:
输入: [-1,-100,3,99] 和 k = 2
输出: [3,99,-1,-100]
解释: 
向右旋转 1 步: [99,-1,-100,3]
向右旋转 2 步: [3,99,-1,-100]

说明:
尽可能想出更多的解决方案，至少有三种不同的方法可以解决这个问题。
要求使用空间复杂度为 O(1) 的 原地 算法。
"""
# No.1:
# class Solution(object):
#     def rotate(self, nums, k):
#         """
#         :type nums: List[int]
#         :type k: int
#         :rtype: None Do not return anything, modify nums in-place instead.
#         """
#         for i in range(k%len(nums)):
#             nums.insert(0,nums.pop())
#         return nums
# s = Solution()
# print(s.rotate([-1,-100,3,99],2))

# No.2:
class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        nlen = len(nums)
        if nlen == k or nlen <= 1 or k < 1:
            return
        if k > nlen:
            k = k%nlen
        # 辗转相除法
        def gcd(q,p):
            tmp = q % p
            while tmp:
                q,p = p,tmp
                tmp = q % p
            return p
        count = gcd(nlen,k)

        # 旋转数组
        for i in range(count):
            start = i
            x = (start + k) % nlen
            tmp = nums[start]
            while True:
                nums[x],tmp = tmp,nums[x]
                if x == start:
                    break
                x = (x + k)% nlen
        return nums

s = Solution()
print(s.rotate([1,2,3,4,5,6,7],3))