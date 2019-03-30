"""
给定一个数组序列，对于所有的子区间。计算子区间中最小值与总值的乘积。
比较所有子区间的所得值，输出最大的那个
"""
def min_sum_max(l):
    n = len(l)
    li = []
    count = 1
    l.sort(reverse = True)
    while count <= n:
        ll = l[:count]
        li.append(min(ll)*sum(ll))
        count += 1
    return max(li)


if __name__ == "__main__":
    a = [6, 2, 1]
    print(min_sum_max(a))