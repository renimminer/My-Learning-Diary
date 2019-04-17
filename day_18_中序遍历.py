# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
"""
执行用时 : 56 ms, 在Binary Tree Inorder Traversal的Python3提交中击败了51.96% 的用户
内存消耗 : 13.3 MB, 在Binary Tree Inorder Traversal的Python3提交中击败了14.25% 的用户
"""

class Solution:
    def __init__(self):
        self.result = []
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if root is None:
            return []  # 核心在这里，题目要求返回的是一个列表
        self.inorderTraversal(root.left)
        self.result.append(root.val)
        self.inorderTraversal(root.right)
        return self.result