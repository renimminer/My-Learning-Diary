class Solution:
    """
    给定正整数 N，返回小于等于 N 且具有至少 1 位重复数字的正整数
    """
    def numDupDigitsAtMostN(self, n):
        if n < 11:
            return 0
        count = 0
        i = 11
        while i <= n:
            if len(set(str(i))) < len(str(i)):
                count += 1
            i += 1
        return count


if __name__ == "__main__":
    solution = Solution()
    print(solution.numDupDigitsAtMostN(725799))

