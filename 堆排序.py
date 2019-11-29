# # 打印树
# import math
#
#
#
# def print_tree(array: list, unit_width=2):
#     length = len(array)
#     depth = math.ceil(math.log2(length))
#     index = 1
#
#     space = ' ' * unit_width
#     for i in range(depth-1, -1, -1):
#         pre = 2 ** i - 1
#         print(pre * space, end='')
#         offset = 2 ** (depth - i - 1)
#         line = array[index:index + offset]
#         interval = (2 * pre + 1) * space
#         print(interval.join(map(lambda x: '{:2}'.format(x), line)))
#         index += offset
#
#     return array

# origin = [0,30, 20, 80, 40, 50, 10, 60, 70, 90]
# total = len(origin) - 1
# # print(origin, total)
# # print_tree(origin)
#
# def heap_adjust(total, i, array:list):
#     while 2 * i <= total:
#         lchild_index = 2 * i
#         max_child_index = lchild_index
#         if total > lchild_index and array[lchild_index + 1] > array[lchild_index]:
#             max_child_index = lchild_index + 1
#
#         if array[max_child_index] > array[i]:
#             array[max_child_index], array[i] = array[i], array[max_child_index]
#             i = max_child_index
#         else:
#             break
#
# # heap_adjust(origin, total, total//2)
# # print('-'*30)
# # print(origin)
# # print_tree(origin)
#
# def max_heap(total, array:list):
#     for i in range(total//2, 0, -1):
#         heap_adjust(total, i, array)
#     return array
#
# print_tree(max_heap(total, origin))
#
# def sort(total,array:list):
#     while total > 1:
#         array[1], array[total] = array[total], array[1]
#         total -= 1
#         if total == 2 and array[total] >= array[total -1]:
#             break
#         heap_adjust(total, 1, array)
#     return array
#
# print_tree(sort(total, origin))
# print(origin)


import math
origin = [0, 30, 20, 80, 40, 50, 10, 60, 70, 90]


# 打印树，方便观察结果
def print_tree(array, unit_width=2):
    length = len(array)
    depth = math.ceil(math.log2(length))  # 本来应该 length + 1，但是由于上面length 加了一个0，所以这里不加
    # width = 2 ** depth - 1  # 宽度为最后一排站满数和空格的个数，这里用不上
    space = ' ' * unit_width  # 中间间隔的空格单位个数 以及 外部空格 的单位大小
    index = 1  # 因为插入了一个0，所以从1开始
    count = 0  # 配合索引计算步长，进行切片，较为简单的一种,记得最后 += 1

    for i in range(depth, -1, -1):
        pre = 2 ** i - 1
        print(space * pre, end='')
        # offset = 2 ** (depth -i -1)  # 开始应该从1,2,3,4=>depth从3,2,1,0 得到关系 2**(depth-i-1)
        sept = 2 ** count
        line = map(str, array[index: index + sept])
        interval = (2 * pre + 1) * space
        print(interval.join(line))
        index += sept
        count += 1
    print('=' * 30)
    return array


print_tree(origin)


# 进行调整，左右比较，父子比较
def heap_adjust(i, total, array):
    count = 0
    while 2 * i <= total:  # 如果 2i =< n 那么这个叶子结点 i,一定有左孩子结点 索引为2i
        lchild_index = 2 * i
        max_child_index = lchild_index  # 假设最大索引为左子孩子结点

        count += 1
        print_tree(array)
        print(count)

        # 如果 存在 右子孩子结点，而且右子孩子比左子孩子大，那么索引交换
        if total > max_child_index and array[lchild_index + 1] > array[lchild_index]:
            max_child_index = lchild_index + 1
        # 如果最大索引结点的数 > 根结点的数，那么交换
        if array[max_child_index] > array[i]:
            array[max_child_index], array[i] = array[i], array[max_child_index]

            i = max_child_index
        else:
            break


    return array


total = len(origin) - 1
heap_adjust(4, total, origin)
# print_tree(heap_adjust(4, total, origin))


# 定义一个循环调整，上面的定义只是做了一次交换，通过下面这个函数，不断调整新的结点作为起点，进行交换
# 最终构建出一个大顶堆
def max_heap(array, total):
    for i in range(total//2, 0, -1):
        heap_adjust(i, total, array)
    return array


max_heap(origin, total)
# print_tree(max_heap(origin, total))


# 排序，默认按照升序，将根结点和n交换，并将n -1，然后重新构建大顶堆，循环进行
def sort(array, total):
    while total > 1:  # 如果总数大于 1 就继续进行
        array[total], array[1] = array[1], array[total]  # 根 和 n 交换
        total -= 1
        if total == 2 and array[total] >= array[total - 1]:  # 如果剩下两个数而且根大于第二个，不交换
            break
        heap_adjust(1, total, array)  # 调用调整函数，因为之前max_heap已经生产了一个大顶堆，所以直接进行调整
    return array


sort(origin, total)
# print_tree(sort(origin, total))
print(origin[1:])
