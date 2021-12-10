"""
给你两个有序整数数组 nums1 和 nums2，请你将 nums2 合并到 nums1 中，使 nums1 成为一个有序数组。

说明：
初始化 nums1 和 nums2 的元素数量分别为 m 和 n 。
你可以假设 nums1 有足够的空间（空间大小大于或等于 m + n）来保存 nums2 中的元素。

示例：
输入：
nums1 = [1,2,3,0,0,0], m = 3
nums2 = [2,5,6],       n = 3
输出：[1,2,2,3,5,6]
 
提示：
-10^9 <= nums1[i], nums2[i] <= 10^9
nums1.length == m + n
nums2.length == n
"""

# No.1
# class Solution(object):
#     def merge(self, nums1, m, nums2, n):
#         """
#         :type nums1: List[int]
#         :type m: int
#         :type nums2: List[int]
#         :type n: int
#         :rtype: None Do not return anything, modify nums1 in-place instead.
#         """
#         for i in range(n):
#             nums1[m+i] = nums2[i]
#         nums1.sort()
#         return nums1
# s = Solution()
# print(s.merge([1,2,3,0,0,0],3,[2,5,6],3))

# No.2
# 用sorted排序不成功的原因:
# sort()方法是原地排序，会按照你指定的顺序排列数据，使用排序后的数据替换原来的数据。原来的顺序会丢失。sorted() BIF内置函数， 是复制排序，
# 会按照你指定的顺序排列数据，然后返回原数据的一个有序副本。原来的顺序会保留下来。
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        nums1[m:] = nums2[:]
        nums1.sort()
        return nums1
s = Solution()
print(s.merge([1,2,3,0,0,0],3,[2,5,6],3))