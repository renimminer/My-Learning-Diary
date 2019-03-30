# 有二维平面整数点集（x，y），输出最大的点的集合（最大点是指该点的右上方没有点）
def ji_he(j):
    n = len(j)
    left = []
    right = []
    for i in range(n):
        left.append(j[i][0])
    for z in range(n):
        right.append(j[z][1])
    print(left)
    print(right)
    left1 = left.copy()
    right1 = right.copy()
    # 准备x,y坐标序列的备份，升序排列
    left1.sort(reverse=True)
    right1.sort()
    print(left1)
    print(right1)
    # 对于x序列，最右端的点一定入选。依次往左看，若左边点高于右边点，入选
    list_result = [(left1[0], right[left.index(left1[0])]), ]
    _max = right[left.index(left1[0])]
    for i in left1[1:]:
        if right[left.index(i)] > _max:
            list_result.append((i, right[left.index(i)]))
            _max = right[left.index(i)]
    print(list_result)


if __name__ == "__main__":
    a = [(1, 9), (2, 1), (3, 7), (4, 3), (5, 2), (6, 4), (7, 8), (8, 6), (9, 5)]
    # (1,9),(7,8),(8,6),(9,5)
    ji_he(a)
