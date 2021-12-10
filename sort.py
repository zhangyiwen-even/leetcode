# 1.冒泡，第一轮结束右边的最大
# class Solution(object):
#     def sorted(self,alist):
#         for i in range(len(alist)):
#             for j in range(i,len(alist)):
#                 if alist[i] > alist[j]:
#                     alist[i],alist[j] = alist[j],alist[i]
#         return alist
# s = Solution()
# print(s.sorted([3,2,1,4,5]))

# 2.简单选择，比较+交换，每次挑选最小的放在前面
# class Solution(object):
#     def sorted(self,alist):
#         for i in range(len(alist)):
#             min_element_index = i
#             for j in range(i,len(alist)):
#                 if alist[j] < alist[min_element_index]:
#                     min_element_index = j
#             alist[i],alist[min_element_index] = alist[min_element_index],alist[i]
#         return alist
# s = Solution()
# print(s.sorted([3,1,2,5,4]))

# 3.插入，向前遍历，把本轮选择的元素与已经排好序的元素相比，升序排序
# class Solution(object):
#     def sorted(self,alist):
#         for i in range(len(alist)):
#             for j in range(0,i):
#                 if alist[j] > alist[i]:
#                     alist[i],alist[j] = alist[j],alist[i]
#         return alist
# s = Solution()
# print(s.sorted([3,1,2,5,4]))

# 4.快速，拟定一个中间值，将数据分为两部分，小于中间值的数据放在左边，大于放右边，以这样的方式处理完左右两边的数据
# def quick_sorted(alist):
#     if len(alist) < 2:
#         return alist
#     left_alist = []
#     right_alist = []
#     base_node = alist.pop(0)
#     for i in alist:
#         if i < base_node:
#             left_alist.append(i)
#         else:
#             right_alist.append(i)
#     return quick_sorted(left_alist) + [base_node] + quick_sorted(right_alist)
# print(quick_sorted([6,3,1,2,4,5]))

# 5.希尔,将待排序数组按照步长gap进行分组，然后将每组的元素利用直接插入排序的方法进行排序，每次将gap折半减少，循环以上操作。
# 当gap=1时，利用直接插入完成排序。
# def sorted(alist):
#     length = len(alist)
#     gap = length // 2
#     while gap >= 1:
#         for j in range(gap,length):
#             i = j
#             while(i - gap) >= 0:
#                 if alist[i] < alist[i-gap]:
#                     alist[i],alist[i-gap] = alist[i-gap],alist[i]
#                     i -= gap
#                 else:
#                     break
#         gap //= 2
#     return alist
# print(sorted([4,2,6,1,3,5]))

# 6.归并
# 思想：将N个长度为1的键值，成对合并成N/2个长度为2的键值组
#       将N/2     2                 N/4        4
#         N/4     4                 N/8        8
#         ...
# def merge_sorted(alist):
#     if len(alist) <= 1:
#         return alist
#     middle = len(alist) // 2
#     left_alist = merge_sorted(alist[:middle])
#     right_alist = merge_sorted(alist[middle:])

#     i = j = 0
#     result_list = []
#     while i < len(left_alist) and j < len(right_alist):
#         if left_alist[i] <= right_alist[j]:
#             result_list.append(left_alist[i])
#             i += 1
#         else:
#             result_list.append(right_alist[i])
#             j += 1
#     result_list += left_alist[i:]
#     result_list += right_alist[j:]

#     return result_list

# print(merge_sorted([4,2,6,1,5,3]))

# 7.桶排
# def tong_sort(alist):
#     max_num = max(alist) # 选择一个最大的数
#     bucket = [0]*(max_num+1) # 创建一个元素全为0的列表。当做桶。

#     for i in alist:  # 把所有元素放入桶中，即把对应的元素个数加一
#         bucket[i] += 1
#         sort_nums = []  # 存储桶中的元素

#     for j in range(len(bucket)):   # 取出桶中的元素
#         if bucket[j] != 0:
#             for y in range(bucket[j]):
#                 sort_nums.append(j)
#     return sort_nums
# print(tong_sort([5,3,1,4,2,6]))

# 8.堆排
def heapify_sort(alist,n,i):
    largest = i
    left = 2 * i + 1  
    right = 2 * i + 2

    if left < n and alist[i] < alist[left]:
        largest = left

    if right < n and alist[largest] < alist[right]:
        largest = right

    if largest != i:
        alist[i],alist[largest] = alist[largest],alist[i] # 交换 

        heapify_sort(alist,n,largest)

def heap_sort(alist):
    n = len(alist)

    for i in range(n,-1,-1):
        heapify_sort(alist,n,i)

    # 一个个的交换元素
    for i in range(n-1,0,-1):
        alist[i],alist[0] = alist[0],alist[i] # 交换
        heapify_sort(alist,i,0)

alist = [12,11,13,5,4,6]
heap_sort(alist)
n = len(alist)
for i in range(n):
    print(alist[i])
