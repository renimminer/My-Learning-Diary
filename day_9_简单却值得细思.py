"""
输入: [7,1,5,3,6,4]
输出: 5
解释: 在第 2 天（股票价格 = 1）的时候买入，在第 5 天（股票价格 = 6）的时候卖出，最大利润 = 6-1 = 5 。
     注意利润不能是 7-1 = 6, 因为卖出价格需要大于买入价格。
"""
class Solution:
    def maxProfit(self, prices):
        _min = 99999999
        _max = 0
        for i in range(len(prices)):
            _min = min(_min,prices[i])
            _max = max(_max,prices[i]-_min)
        return _max


if __name__ == "__main__":
    solution = Solution()
    print(solution.maxProfit([7,6,5,4,3,2]))
