class Solution:
    """
    自除数 是指可以被它包含的每一位数除尽的数。

例如，128 是一个自除数，因为 128 % 1 == 0，128 % 2 == 0，128 % 8 == 0。

还有，自除数不允许包含 0 。

给定上边界和下边界数字，输出一个列表，列表的元素是边界（含边界）内所有的自除数。

    """
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        ll = []
        while left <= right:
            if self.iszichu(left) is True:
                ll.append(left)
            left += 1
        return ll

    def iszichu(self, x):
        li = list(str(x))
        if "0" in li:
            return False
        for i in li:
            if x % int(i) != 0:
                return False
        return True


if __name__ == "__main__":
    solution = Solution()
    print(solution.selfDividingNumbers(1,22))