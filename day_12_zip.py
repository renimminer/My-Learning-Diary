class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        res = ""
        if len(strs) == 0:
            return ""
        for each in zip(*strs):  # 传递多个参数
            if len(set(each)) == 1:
                res += each[0]
            else:
                return res
        return res


if __name__ == "__main__":
    solution = Solution()
    print(solution.longestCommonPrefix(["flower","flow","flight"]))