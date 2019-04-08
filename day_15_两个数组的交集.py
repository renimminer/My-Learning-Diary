"""
给定两个数组，编写一个函数来计算它们的交集。

示例 1:

输入: nums1 = [1,2,2,1], nums2 = [2,2]
输出: [2]
O(n)
执行用时 : 88 ms, 在Intersection of Two Arrays的Python3提交中击败了22.42% 的用户
内存消耗 : 13.1 MB, 在Intersection of Two Arrays的Python3提交中击败了0.96% 的用户
"""
# 可以用位运算符&改进


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if nums1 == [] or nums2 == []:
            return []
        res = set()
        for i in nums1:
            if i in nums2:
                res.add(i)
        return list(res)
