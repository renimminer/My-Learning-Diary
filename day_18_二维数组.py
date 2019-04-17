class Solution:
    # array 二维列表
    def Find(self, target, array):
        # write code here
        i = 0
        J = len(array[0])-1
        I = len(array)-1
        j = J
        while i <= I and j >= 0:
            cur = array[i][j]
            if target == cur:
                return True
            elif target > cur:
                i += 1
            else:
                j -= 1
        return False


if __name__ == "__main__":
    solution = Solution()
    print(solution.Find(7,[[1,2,8,9],[2,4,9,12],[4,7,10,13],[6,8,11,15]]))