"""
在一排座位（ seats）中，1 代表有人坐在座位上，0 代表座位上是空的。

至少有一个空座位，且至少有一人坐在座位上。

亚历克斯希望坐在一个能够使他与离他最近的人之间的距离达到最大化的座位上。

返回他到离他最近的人的最大距离。
O(n)
执行用时 : 76 ms, 在Maximize Distance to Closest Person的Python3提交中击败了61.59% 的用户
内存消耗 : 13.8 MB, 在Maximize Distance to Closest Person的Python3提交中击败了0.00% 的用户
"""
class Solution(object):
    def maxDistToClosest(self, seats):

        # 得出列表中所有元素为1的下标
        l = []
        for key,value in enumerate(seats):
            if value == 1:
                l.append(key)

        # 得出坐在两端时，与最近人的最远距离
        n = len(seats)
        front = l[0]-0
        rear = n-1 - l[-1]
        # 找出中间位置时，与最近人的最远距离
        _max = 0
        for i in range(1, len(l)):
            _max = max(_max, l[i] - l[i - 1])
        return max(_max // 2,front,rear)


if __name__ == "__main__":
    solution = Solution()
    print(solution.maxDistToClosest([1,0,0,0]))