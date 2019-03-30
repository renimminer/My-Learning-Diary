class Solution:
    def findContentChildren(self, g, s):
        if g == [] or s == []:
            return 0
        s.sort(reverse=True)
        g.sort(reverse=True)
        i = 0
        count = 0
        while i < len(s):
            if g == []:
                return count
            elif s[i] > g[0]:
                count += 1
                g.pop(0)
            else:
                g.pop(0)
            i += 1
        return count


if __name__ == "__main__":
    solution = Solution()
    print(solution.findContentChildren([1,2,3], [1,1]))