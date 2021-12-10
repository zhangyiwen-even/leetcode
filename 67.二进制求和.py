"""
给你两个二进制字符串，返回它们的和（用二进制表示）。
输入为 非空 字符串且只包含数字 1 和 0。
示例 1:
输入: a = "11", b = "1"
输出: "100"

示例 2:
输入: a = "1010", b = "1011"
输出: "10101"
提示：
每个字符串仅由字符 '0' 或 '1' 组成。
1 <= a.length, b.length <= 10^4
字符串如果不是 "0" ，就都不含前导零。
"""
# 思路：先将二进制转换为十进制，求和，将和再次转换为二进制，输出。
# 使用Python内置函数：bin()、oct()、int()、hex()可实现进制转换。
    #      	  2进制	            8进制	         10进制	            16进制
    # 2进制	   -	            bin(int(x, 8))	 bin(int(x, 10))	bin(int(x, 16))
    # 8进制	   oct(int(x, 2))	 -	             oct(int(x, 10))	oct(int(x, 16))
    # 10进制	   int(x, 2)	    int(x, 8)	      -              	int(x, 16)
    # 16进制     hex(int(x, 2))	hex(int(x, 8))	 hex(int(x, 10))	-
class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        int_a = int(a,2)
        int_b = int(b,2)
        sum =  int_a+int_b
        return bin(sum).split('b')[1]
s = Solution()
print(s.addBinary("11","1"))


