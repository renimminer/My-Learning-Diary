class Solution:
    """
    编写一个函数来查找字符串数组中的最长公共前缀。

如果不存在公共前缀，返回空字符串 ""。

示例 1:

输入: ["flower","flow","flight"]
输出: "fl"
    """
    def longestCommonPrefix(self, strs):
        if strs == []:
            return ""
        elif len(strs) == 1:
            return strs[0]
        elif len(set(strs)) == 1:
            return strs[0]
        i = 1
        li = []
        while i >= 0:
            for j in strs:
                li .append(j[:i])
            if len(set(li)) != 1:
                break
            elif "" in set(li):
                return ""
            li = []
            i += 1
        return strs[0][:i-1]


if __name__ == "__main__":
    solution = Solution()
    print(solution.longestCommonPrefix(["c", "c"]))