"""
给定一个由 整数 组成的 非空 数组所表示的非负整数，在该数的基础上加一。
最高位数字存放在数组的首位， 数组中每个元素只存储单个数字。
你可以假设除了整数 0 之外，这个整数不会以零开头。

示例 1：
输入：digits = [1,2,3]
输出：[1,2,4]
解释：输入数组表示数字 123。

示例 2：
输入：digits = [4,3,2,1]
输出：[4,3,2,2]
解释：输入数组表示数字 4321。

示例 3：
输入：digits = [0]
输出：[1]
 
提示：
1 <= digits.length <= 100
0 <= digits[i] <= 9
"""

# No.1 自己的方法:没有ac，因为测试用例为[0,0]时，输出的结果应该是[0,1]而不是[1],测试用例跟题干都矛盾了
# class Solution(object):
#     def plusOne(self, digits):
#         """
#         :type digits: List[int]
#         :rtype: List[int]
#         """
#         # int转为list
#         int_d = int(''.join([str(i) for i in digits]))
#         # return int_d
#         # 加1
#         sum1 = int_d + 1
#         # 输出 list转为int
#         return [int(j) for j in str(sum1)]
# 
#         # 上面写成一行就是:
#         return list(map(int,list(str(int(''.join(map(str,digits))) + 1))))
#
# s = Solution()
# print(s.plusOne([0,0]))

# No.2 ac的答案:
# 逢9进位,否则当前位+1后直接return

class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        n = len(digits)
        for i in range(n-1,-1,-1):
            if digits[i] == 9:
                digits[i] = 0
            else:
                digits[i] += 1
                return digits
        return [1] + digits
s = Solution()
print(s.plusOne([9,9]))