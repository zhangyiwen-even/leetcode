"""
给你一个整数数组 arr，请你判断数组中是否存在连续三个元素都是奇数的情况：
如果存在，请返回 true ；否则，返回 false 。

示例 1：
输入：arr = [2,6,4,1]
输出：false
解释：不存在连续三个元素都是奇数的情况。

示例 2：
输入：arr = [1,2,34,3,4,5,7,23,12]
输出：true
解释：存在连续三个元素都是奇数的情况，即 [5,7,23] 。
 
提示：
1 <= arr.length <= 1000
1 <= arr[i] <= 1000
"""

# class Solution(object):
#     def threeConsecutiveOdds(self, arr):
#         """
#         :type arr: List[int]
#         :rtype: bool
#         """
#         # 列表长度小于3 则不需要判断 直接false
#         if len(arr) < 3:
#             return False
#         for i in range(1,len(arr)-1):
#             if (arr[i - 1] & 1) and (arr[i] & 1) and (arr[i + 1] & 1):
#                 return True
#         return False
# s = Solution()
# print(s.threeConsecutiveOdds([1,2,34,3,4,5,7,23,12]))

# class Solution(object):
#     def threeConsecutiveOdds(self, arr):
#         """
#         :type arr: List[int]
#         :rtype: bool
#         """
#         count = 0
#         for i in range(len(arr)):
#             if arr[i] % 2 != 0:
#                 count += 1
#             else:
#                 count = 0
#             if count == 3:
#                 return True
#         return False
# s = Solution()
# print(s.threeConsecutiveOdds([1,2,34,3,4,5,7,23,13]))

class Solution(object):
    def threeConsecutiveOdds(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        count = 0
        for i in range(len(arr)):
            if arr[i] % 2 != 0:
                count += 1
            else:
                # 如果为偶数 则重置count的值 
                count = 0
            if count == 3:
                return True
        return False
s = Solution()
print(s.threeConsecutiveOdds([1,2,34,3,4,5,7,23,13]))
