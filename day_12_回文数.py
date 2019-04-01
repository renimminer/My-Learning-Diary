class Solution:
    """
    判断一个整数是否是回文数。回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。

示例 1:

输入: 121
输出: true
    """
    def isPalindrome(self, x: int) -> bool:
        if x == []:
            return False
        x = list(str(x))
        n = len(x)
        while n > 1:
            if x[0] == x[-1]:
                x.pop()
                x.pop(0)
                n = len(x)
            else:
                return False
        return True


if __name__ == "__main__":
    solution = Solution()
    solution.isPalindrome(121)