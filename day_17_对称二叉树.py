# Definition for a binary tree node.
"""
递归的时间复杂度？？O（n）
给定两个二叉树，编写一个函数来检验它们是否相同。

如果两个树在结构上相同，并且节点具有相同的值，则认为它们是相同的。
执行用时 : 52 ms, 在Same Tree的Python3提交中击败了77.57% 的用户
内存消耗 : 13 MB, 在Same Tree的Python3提交中击败了76.02% 的用户
"""
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        # p_poit = p
        # q_poit = q
        # if p_poit is None and q_poit is None:
        #     return True
        # elif p_poit is None and q_poit is None:
        #     return False
        # if p_poit.val != q_poit.val:
        #     return False


        if p is None and q is None:
            return True
        elif p is None or q is None:
            return False
        if p.val != q.val:
            return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
    """
    在递归过程中，得到的返回值只会返回到循环中的上一层，
    只有在最外层加上return，才能在递归中有结果时，直接的跳出全部的循环
    """





if __name__ == "__main__":
    p = TreeNode(1)
    p.left = TreeNode(1)
    #p.right = TreeNode(3)
    q = TreeNode(1)
    q.left = None
    q.right = TreeNode(1)
    solution = Solution()
    print(solution.isSameTree(p,q))