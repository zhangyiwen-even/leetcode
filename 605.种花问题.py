"""
假设你有一个很长的花坛，一部分地块种植了花，另一部分却没有。
可是，花卉不能种植在相邻的地块上，它们会争夺水源，两者都会死去。
给定一个花坛（表示为一个数组包含0和1，其中0表示没种植花，1表示种植了花），和一个数 n 。
能否在不打破种植规则的情况下种入 n 朵花？能则返回True，不能则返回False。

示例 1:
输入: flowerbed = [1,0,0,0,1], n = 1
输出: True

示例 2:
输入: flowerbed = [1,0,0,0,1], n = 2
输出: False

注意:
数组内已种好的花不会违反种植规则。
输入的数组长度范围为 [1, 20000]。
n 是非负整数，且不会超过输入数组的大小。
"""
# 防御式编程思想： 在flowerbed列表两端各增加一个0，
# 这样处理的好处在于不用考虑边界条件，任意位置处只要连续出现3个0就可以栽上一棵花。
class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        tmp = [0] + flowerbed + [0]
        for i in range(1,len(tmp)-1):
            if tmp[i-1] == 0 and tmp[i] == 0 and tmp[i+1] == 0:
                tmp[i] = 1 # 在i处栽上花
                n -= 1
        return n <= 0  # n小于等于0，表示可以栽完花
s = Solution()
print(s.canPlaceFlowers([0,1,0],1))