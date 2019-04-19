"""
C市现在要转移一批罪犯到D市，C市有n名罪犯，按照入狱时间有顺序，另外每个罪犯有一个罪行值，值越大罪越重。
现在为了方便管理，市长决定转移入狱时间连续的c名犯人，同时要求转移犯人的罪行值之和不超过t，
问有多少种选择的方式（一组测试用例可能包含多组数据，请注意处理）？
第一行数据三个整数:n，t，c(1≤n≤2e5,0≤t≤1e9,1≤c≤n)
第二行按入狱时间给出每个犯人的罪行值ai(0≤ai≤1e9)
"""
# 3 100 2
# 1 2 3
while True:
    n, t, c = map(int, input().split())
    a = list(map(int, input().split()))
    queue = a[:c]
    count = 0
    s = sum(queue)
    for i in range(c, n):
        if s <= t:
            count += 1
        s -= a[i-c]       # queue.pop(0)    改进后的核心在这里，起初使用滑动窗口，太过浪费资源                            #
        s += a[i]         # queue.append(i)    现在算是动态规划了
    if sum(queue) <= t:
        count += 1
    print(count)


# def Solu(nums, t, n, c):
#     dp = sum(nums[i] for i in range(c))
#     res = 0
#     for i in range(c, n):
#         if dp <= t:
#             res += 1
#         dp = dp + nums[i] - nums[i - c]
#     if dp <= t:
#         res += 1
#     print(res)

#
# while True:
#     try:
#         n, t, c = map(int, input().split())
#         nums = list(map(int, input().split()))
#         Solu(nums, t, n, c)
#     except:
#         break
