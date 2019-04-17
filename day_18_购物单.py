

"""
输入
输入中有多组测试数据。每组测试数据的第一行为两个整数n和m（1=＜n, m=＜1000），分别表示价签的数量以及小B的购买清单中所列的物品数。第二行为空格分隔的n个正整数，表示货架上各类物品的价格，每个数的大小不超过100000。随后的m行为购买清单中物品的名称，所有物品名称为非空的不超过32个拉丁字母构成的字符串，保证清单中不同的物品种类数不超过n，且商店有小B想要购买的所有物品。

样例输入
5 3
4 2 1 10 5
apple
orange
mango
6 5
3 5 1 6 8 1
peach
grapefruit
banana
orange
orange

输出
对每组测试数据，在单独的行中输出两个数a和b，表示购买清单上所有的物品可能需要的最小和最大费用。

样例输出
7 19
11 30
"""
def costfunction(price, m, n):
    cost = 0
    for i in range(n):
        cost += m[i]*price[i]
    return cost


while True:
    n, m = input().split()
    n = int(n)
    m = int(m)
    prices = input().split()
    while m > 1:
        prices.extend(input().split())
        m -= 1
    price1 = []
    for p in prices:
        price1.append(int(p))
    # 判定是否有重复物品
    item = input().split()
    dic = {}
    for i in item:
        if i not in dic:
            dic[i] = 1
        else:
            dic[i] += 1
    m = list(dic.values())
    m.sort(reverse=True)
    n = len(m)
    price2 = price1.copy()
    price1.sort()
    price2.sort(reverse=True)
    min_sum = costfunction(price1, m, n)
    max_sum = costfunction(price2, m, n)
    print(min_sum, max_sum)
    # peach grapefruit banana orange orange
    # apple orange mango
