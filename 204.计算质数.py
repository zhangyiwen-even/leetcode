"""
统计所有小于非负整数 n 的质数的数量。

示例 1：
输入：n = 10
输出：4
解释：小于 10 的质数一共有 4 个, 它们是 2, 3, 5, 7。

示例 2：
输入：n = 0
输出：0

示例 3：
输入：n = 1
输出：0

提示：
0 <= n <= 5 * 106
"""
# 测试用例可以过 但是提交显示超时
# class Solution(object):
#     def countPrimes(self, n):
#         """
#         :type n: int
#         :rtype: int
#         """
#         # 将质数输出到列表里，求列表长度
#         alist = []
#         i = 2
#         for i in range(2,n):
#             j = 2
#             for j in range(2,i):
#                 if i % j == 0:
#                     break
#             else:
#                 alist.append(i)
#         return len(alist)
# s = Solution()
# print(s.countPrimes(1))

# 大神的答案:
# 这题搜到一个非常牛逼的算法,叫做厄拉多塞筛法. 比如说求20以内质数的个数,首先0,1不是质数.2是第一个质数,然后把20以内所有2的倍数划去.2后面紧跟的数即为下一个质数3,然后把3所有的倍数划去.
# 3后面紧跟的数即为下一个质数5,再把5所有的倍数划去.以此类推.
# 代码的实现用了很好的技巧:
class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 3:
            return 0
        else:
            # 首先生成一个全为1的列表
            output = [1] * n
            # 因为0和1不是质数，所以列表的前两个位置赋值为0
            output[0],output[1] == 0,0
            # 此时从index = 2开始遍历，output[2] == 1，即表明第一个质数为2，然后将2的倍数对应的索引
            # 全部赋值为0，此时output[3] == 1，即表明下一个质数为3,同样划去3的倍数。以此类推
            for i in range(2,int(n**0.5)+1):
                if output[i] == 1:
                    output[i*i:n:i] = [0] * len(output[i*i:n:i])
            # 最后output中的数字1表明该位置上的索引数为质数，然后求和即可。
        return sum(output)
s = Solution()
print(s.countPrimes(10))