"""
有一堆石头，每块石头的重量都是正整数。
每一回合，从中选出两块 最重的 石头，然后将它们一起粉碎。
假设石头的重量分别为 x 和 y，且 x <= y。那么粉碎的可能结果如下：
如果 x == y，那么两块石头都会被完全粉碎；
如果 x != y，那么重量为 x 的石头将会完全粉碎，而重量为 y 的石头新重量为 y-x。
最后，最多只会剩下一块石头。返回此石头的重量。如果没有石头剩下，就返回 0。

示例：

输入：[2,7,4,1,8,1]
输出：1
解释：
先选出 7 和 8，得到 1，所以数组转换为 [2,4,1,1,1]，
再选出 2 和 4，得到 2，所以数组转换为 [2,1,1,1]，
接着是 2 和 1，得到 1，所以数组转换为 [1,1,1]，
最后选出 1 和 1，得到 0，最终数组转换为 [1]，这就是最后剩下那块石头的重量。
 
提示：
1 <= stones.length <= 30
1 <= stones[i] <= 1000
"""

# Python中列表（list）的实现其实是一个数组，当要查找某一个元素的时候时间复杂度是O(n)，
# 使用list.index()方法，但是随着数据量的上升，list.index()的性能也逐步下降，
# 所以我们需要使用bisect模块来进行二分查找，前提我们的列表是一个有序的列表。

# 用bisect.insort插入新元素
# 排序很耗时，因此在得到一个有序序列之后，我们最好能够保持它的有序。bisect.insort就是为这个而存在的
# insort(seq, item)把变量item插入到序列seq中，并能保持seq的升序顺序
import bisect
class Solution(object):
    def lastStoneWeight(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        stones.sort()
        while len(stones) > 1:
            a = stones.pop()
            b = stones.pop()
            if a == b:
                continue
            else:
                bisect.insort(stones,a-b)
        
        if len(stones) == 1:
            return stones[0]
        else:
            return 0
s = Solution()
print(s.lastStoneWeight([2,7,4,1,8,1]))
