# class Solution(object):
#     def uniquePaths(self, m, n):
#
#         # if m == 1:
#         #     return 1
#         # elif n == 1:
#         #     return 1
#         # import numpy as np
#         # p_array = np.zeros((m, n))
#         # p_array[0, :] = 1
#         # p_array[:, 0] = 1
#         # for i in range(1, m):
#         #     for j in range(1, n):
#         #         p_array[i, j] = p_array[i-1, j] + p_array[i, j-1]
#         # return p_array[m-1, n-1]
"""
一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为“Start” ）。

机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为“Finish”）。

问总共有多少条不同的路径？

执行用时 : 52 ms, 在Unique Paths的Python3提交中击败了78.71% 的用户
内存消耗 : 13 MB, 在Unique Paths的Python3提交中击败了84.06% 的用户
"""
class Solution(object):
    def uniquePaths(self, m, n):
        if m == 1:
            return 1
        elif n == 1:
            return 1
        p_array = [[0]*n]*m  # 二维累计数组
        p_array[0] = [1]*n
        for i in p_array:
            i[0] = 1
        for i in range(1, m):
            for j in range(1, n):
                p_array[i][j] = p_array[i-1][j] + p_array[i][j-1] # 核心F(m,n)=F(m-1,n)+F(n,m-1)
        return p_array[m-1][n-1]


if __name__ == "__main__":
    solution = Solution()
    print(solution.uniquePaths(7, 3))


