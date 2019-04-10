"""
O(n)
执行用时 : 56 ms, 在Baseball Game的Python3提交中击败了21.17% 的用户
内存消耗 : 13.3 MB, 在Baseball Game的Python3提交中击败了0.00% 的用户
"""
class Solution:
    """
    你现在是棒球比赛记录员。
给定一个字符串列表，每个字符串可以是以下四种类型之一：
1.整数（一轮的得分）：直接表示您在本轮中获得的积分数。
2. "+"（一轮的得分）：表示本轮获得的得分是前两轮有效 回合得分的总和。
3. "D"（一轮的得分）：表示本轮获得的得分是前一轮有效 回合得分的两倍。
4. "C"（一个操作，这不是一个回合的分数）：表示您获得的最后一个有效 回合的分数是无效的，应该被移除。

每一轮的操作都是永久性的，可能会对前一轮和后一轮产生影响。
你需要返回你在所有回合中得分的总和。
    """
    def calPoints(self, ops: List[str]) -> int:
        stack = []
        n = len(ops)
        for i in range(n):
            if ops[i] == "+":
                stack.append(stack[len(stack)-1]+stack[len(stack)-2])
            elif ops[i] == "D":
                stack.append(stack[len(stack)-1]*2)
            elif ops[i] == "C":
                stack.pop()
            else:
                stack.append(int(ops[i]))
        return sum(stack)