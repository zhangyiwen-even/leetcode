"""
给定一个大小为 n 的数组，找到其中的多数元素。多数元素是指在数组中出现次数大于 ⌊ n/2 ⌋ 的元素。
你可以假设数组是非空的，并且给定的数组总是存在多数元素。

示例 1:
输入: [3,2,3]
输出: 3

示例 2:
输入: [2,2,1,1,1,2,2]
输出: 2
"""
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 转换为字典，key是元素，value是出现的次数，输出value值最大的key。
        dict1 = {}
        for i in nums:
            if i not in dict1:
                dict1[i] == 1
            else:
                dict1[i] += 1
        return dict1
s = Solution()
print(s.majorityElement([3,2,3]))