"""
设计一个支持 push ，pop ，top 操作，并能在常数时间内检索到最小元素的栈。
push(x) —— 将元素 x 推入栈中。
pop() —— 删除栈顶的元素。
top() —— 获取栈顶元素。
getMin() —— 检索栈中的最小元素。
 
示例:
输入：
["MinStack","push","push","push","getMin","pop","top","getMin"]
[[],[-2],[0],[-3],[],[],[],[]]

输出：
[null,null,null,null,-3,null,0,-2]

解释：
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin();   --> 返回 -3.
minStack.pop();
minStack.top();      --> 返回 0.
minStack.getMin();   --> 返回 -2.
 
提示：
pop、top 和 getMin 操作总是在 非空栈 上调用。
"""
# 自己的方法，可以ac
# from queue import Queue
# class MinStack(object):
#     def __init__(self):
#         """
#         initialize your data structure here.
#         """
#         # 初始化一个栈
#         self.data = []
#     def push(self, x):
#         """
#         :type x: int
#         :rtype: None
#         """
#         # 进栈
#         self.data.append(x)
#     def pop(self):
#         """
#         :rtype: None
#         """
#         # 出栈
#         self.data.pop()
#     def top(self):
#         """
#         :rtype: int
#         """
#         # 输出最先入栈的元素
#         # 判断栈的长度是否为0
#         if len(self.data) ==0:
#             return None
#         else:
#             return self.data[-1]
#     def getMin(self):
#         """
#         :rtype: int
#         """
#         # 栈中最小的元素
#         # 判断栈的长度是否为0
#         if len(self.data) == 0:
#             return None
#         else:
#             return min(self.data)
# # Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(1)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
# print(param_3,param_4)


# python的标准答案:
# 利用一个最小值栈，push和pop时根据值判断进行维护
class MinStack(object):    
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.min_list = []

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.stack.append(x)
        if not self.min_list:
            self.min_list.append(x)
        elif x <= self.min_list[-1]:
            self.min_list.append(x)

    def pop(self):
        """
        :rtype: None
        """
        n = self.stack.pop()
        if n == self.min_list[-1]:
            self.min_list.pop()

    def top(self):
        """
        :rtype: int
        """
        if not self.stack:
            return None
        return self.stack[-1]

    def getMin(self):
        """
        :rtype: int
        """
        if not self.min_list:
            return None
        return self.min_list[-1]

# Your MinStack object will be instantiated and called as such:
obj = MinStack()
obj.push(1)
obj.push(2)
obj.push(1)
obj.pop()
param_3 = obj.top()
param_4 = obj.getMin()
print(param_3,param_4)