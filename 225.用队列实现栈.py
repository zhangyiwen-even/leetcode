"""
使用队列实现栈的下列操作：
push(x) -- 元素 x 入栈
pop() -- 移除栈顶元素
top() -- 获取栈顶元素
empty() -- 返回栈是否为空

注意:
你只能使用队列的基本操作-- 也就是 push to back, peek/pop from front, size, 和 is empty 这些操作是合法的。
你所使用的语言也许不支持队列。 你可以使用 list 或者 deque（双端队列）来模拟一个队列 , 只要是标准的队列操作即可。
你可以假设所有操作都是有效的（例如, 对一个空的栈不会调用 pop 或者 top 操作）。
"""
# 提交的时候有问题,仅仅是用到了栈，没有体现出是用队列实现的
# class MyStack(object):
#     def __init__(self):
#         """
#         Initialize your data structure here.
#         """
#         # 定义一个栈
#         self.data = []

#     def push(self, x):
#         """
#         Push element x onto stack.
#         :type x: int
#         :rtype: None
#         """
#         # x元素进栈
#         self.data.append(x)

#     def pop(self):
#         """
#         Removes the element on top of the stack and returns that element.
#         :rtype: int
#         """
#         # 出栈
#         self.data.pop()

#     def top(self):
#         """
#         Get the top element.
#         :rtype: int
#         """
#         #求栈顶元素，最先进栈的元素是栈顶元素
#         if len(self.data) == 0:
#             return None
#         else:
#             return self.data[-1]

#     def empty(self):
#         """
#         Returns whether the stack is empty.
#         :rtype: bool
#         """
#         # 判断栈是否为空
#         if len(self.data) == 0:
#             return True
#         else:
#             return False


# # Your MyStack object will be instantiated and called as such:
# # 测试用例进行测试
# obj = MyStack()
# obj.push(1)
# obj.push(2)
# obj.push(3)
# p2 = obj.pop()
# p3 = obj.top()
# p4 = obj.empty()
# print(p2,p3,p4)

# ac:
# Queue的种类：
# FIFO即First in First Out,先进先出。Queue提供了一个基本的FIFO容器，使用方法很简单,maxsize是个整数，指明了队列中能存放的数据个数的上限。一旦达到上限，插入会导致阻塞，直到队列中的数据被消费掉。
# 如果maxsize小于或者等于0，队列大小没有限制。
# 构造一个优先队列。maxsize用法同上。
# 基本方法：
# 　　 Queue.Queue(maxsize=0)   FIFO， 如果maxsize小于1就表示队列长度无限
#        Queue.LifoQueue(maxsize=0)   LIFO， 如果maxsize小于1就表示队列长度无限
#        Queue.qsize()   返回队列的大小 
#        Queue.empty()   如果队列为空，返回True,反之False 
#        Queue.full()   如果队列满了，返回True,反之False
#        Queue.get([block[, timeout]])   读队列，timeout等待时间 
#        Queue.put(item, [block[, timeout]])   写队列，timeout等待时间 
#        Queue.queue.clear()   清空队列

from queue import Queue
class MyStack(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        # 队列名是q
        self.q = Queue()

    def push(self, x):
        """
        Push element x onto stack.
        :type x: int
        :rtype: None
        """
        # put()函数:写队列,将x写入
        self.q.put(x)
        #qsize(): 返回队列的大小
        for i in range(self.q.qsize()-1):
            # get()函数: 读队列
            self.q.put(self.q.get())

    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        :rtype: int
        """
        self.q.get()

    def top(self):
        """
        Get the top element.
        :rtype: int
        """
        r = self.q.get()
        self.q.put(r)
        for j in range(self.q.qsize()-1):
            self.q.put(self.q.get())
        return r

    def empty(self):
        """
        Returns whether the stack is empty.
        :rtype: bool
        """
        # 判断栈是否为空
        return not self.q.qsize()
# Your MyStack object will be instantiated and called as such:
# 测试用例进行测试
obj = MyStack()
obj.push(1)
obj.push(2)
obj.push(3)
p2 = obj.pop()
p3 = obj.top()
p4 = obj.empty()
print(p2,p3,p4)