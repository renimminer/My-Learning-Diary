class Solution(object):
    def reverse(self, num):
        if str(num)[0] == "-":
            a = "-"
            num = str(num)[1:]
        else:
            a = ""
            num = str(num)
        stack = []
        s = ""
        for n in num:
            stack.append(n)
        while stack != []:
            s += stack.pop()
        s = int(a + s)
        if  -2**31 <= s <= 2**31:
            return s
        else:
            return 0

solution = Solution()
print(solution.reverse(1534236469))
