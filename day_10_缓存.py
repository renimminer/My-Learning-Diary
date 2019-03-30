"""
Python3 抖个机灵， 设置个缓存竟然过了。。。
"""
from functools import lru_cache


class Solution:
    @lru_cache(10**8)
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """

        if n == 1:
            return 1
        elif n == 2:
            return 2
        else:
            return self.climbStairs(n - 1) + self.climbStairs(n - 2)