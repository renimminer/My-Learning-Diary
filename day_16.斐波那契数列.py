"""
O(n)
执行用时 : 52 ms, 在Fibonacci Number的Python3提交中击败了42.56% 的用户
内存消耗 : 13.3 MB, 在Fibonacci Number的Python3提交中击败了100.00% 的用户
"""
class Solution:
    """
    斐波那契数，通常用 F(n) 表示，形成的序列称为斐波那契数列。该数列由 0 和 1 开始，后面的每一项数字都是前面两项数字的和。也就是：

F(0) = 0,   F(1) = 1
F(N) = F(N - 1) + F(N - 2), 其中 N > 1.
给定 N，计算 F(N)。
    """
    def fib(self, N: int) -> int:
        if N == 0:
            return 0
        elif N == 1:
            return 1
        else:
            i = 0
            j = 1
            F = 1
            while F != N:
                i, j = j, i + j
                F += 1
            return j
