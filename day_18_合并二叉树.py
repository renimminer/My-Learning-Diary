"""
给定两个二叉树，想象当你将它们中的一个覆盖到另一个上时，两个二叉树的一些节点便会重叠。

你需要将他们合并为一个新的二叉树。合并的规则是如果两个节点重叠，那么将他们的值相加作为节点合并后的新值，
否则不为 NULL 的节点将直接作为新二叉树的节点。
"""

class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        # 函数的返回值有两种情况，t1与t2都为真，返回两个节点的和。t1与t2不都为真，返回t1与t2中不假的值
        if t1 and t2 :  # 树结构本身可作为逻辑判断语句
            t1.val += t2.val
            t1.left = self.mergeTrees(t1.left, t2.left)  # 将左子树的函数返回值视为树的左子树
            t1.right = self.mergeTrees(t1.right, t2.right)
            return t1
        return t1 or t2  # 返回t1与t2中不假的值


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# class Solution:
#     def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
#         node = TreeNode(0)
#         if t1 == None and t2 == None:
#             return
#         elif t1 == None:
#             t1 = node
#         elif t2 == None:
#             t2 = node
#         t1.val = t1.val + t2.val
#         self.mergeTrees(t1.left,t2.left)
#         self.mergeTrees(t1.right,t2.right)
#         return t1

class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        if t1 == None and t2 == None:
            return None
        elif t1 == None and t2 != None:
            return t2
        elif t1 != None and t2 == None:
            return t1
        node = TreeNode(0)
        if t1 == None and t2 == None:
            return
        if t1.left == None and t2.left != None:
            t1.left = node
        if t1.left != None and t2.left == None:
            t2.left = node
        if t1.right == None and t2.right != None:
            t1.right = node
        if t1.right != None and t2.right == None:
            t2.right = node
        t1.val = t1.val + t2.val
        self.mergeTrees(t1.left,t2.left)
        self.mergeTrees(t1.right,t2.right)
        return t1


if __name__ == "__main__":
    t1 = TreeNode(1)
    t1.left = TreeNode(3)
    t1.left.left = TreeNode(5)
    t1.right = TreeNode(2)
    t2 = TreeNode(2)
    t2.left = TreeNode(1)
    t2.left.right = TreeNode(4)
    t2.right = TreeNode(3)
    t2.right.right = TreeNode(7)
    sloution = Solution()
    print(sloution.mergeTrees(t1, t2))