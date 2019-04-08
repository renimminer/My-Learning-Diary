class Solution:
    """
    给定一个非负整数 N，找出小于或等于 N 的最大的整数，同时这个整数需要满足其各个位数上的数字是单调递增。

（当且仅当每个相邻位数上的数字 x 和 y 满足 x <= y 时，我们称这个整数是单调递增的。）
    """
    def monotoneIncreasingDigits(self, N):
        li = list(str(N))
        l = li.copy()
        n = len(li)
        res = []
        j = []
        if li == l.sort():
            return N
        for i in range(n-1):
            if int(li[i]) < int(li[i+1]):
                res.append(li[i])
            else:
                res.append(str(int(li[i])-1))
                j.append(i+1)
        _n = j[0]
        re = ""
        for i in res:
            re += i
        re +="9"*(n-_n)
        return int(re)


if __name__ == "__main__":
    solution = Solution()
    print(solution.monotoneIncreasingDigits(332))