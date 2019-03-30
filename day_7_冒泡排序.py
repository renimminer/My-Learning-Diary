# 冒泡排序
def qq_sort(l):
    for i in range(len(l)-1, 0, -1):
        for j in range(i):
            if l[j] > l[j+1]:
                l[j], l[j+1] = l[j+1], l[j]
    return l


print(qq_sort([2, 3, 1, 4, 6, 5]))

# 改进的冒泡排序, 加入一个校验, 如果某次循环发现没有发生数值交换, 直接跳出循环
