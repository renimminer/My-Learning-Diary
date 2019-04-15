"""
给定一个二叉树，检查它是否是镜像对称的。

例如，二叉树 [1,2,2,3,4,4,3] 是对称的。

    1
   / \
  2   2
 / \ / \
3  4 4  3
但是下面这个 [1,2,2,null,3,null,3] 则不是镜像对称的:

    1
   / \
  2   2
   \   \
   3    3
执行用时 : 60 ms, 在Symmetric Tree的Python3提交中击败了71.10% 的用户
内存消耗 : 13.2 MB, 在Symmetric Tree的Python3提交中击败了32.24% 的用户
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if root is None:
            return True
        if root.left is None and root.right is None:
            return True
        elif root.left is None or root.right is None:
            return False
        # 递归函数无法直接判断是否相等，（设定递归函数的返回值，进行相似度判定）
        if root.left.val == root.right.val and self.left_tree(root.left,[]) == self.right_tree(root.right,[]):
            return True

        else:
            return False

    def left_tree(self,root,res):  # 通过多增加一个参数，可以达到接收缓存的目的（想以列表的形式接收遍历所得值）
        if root == None:
            res.append(None)   # 通过增加None可以用None表示，打印出二叉树缺少的左（右）一段
            return
        res.append(root.val)
        self.left_tree(root.left,res)
        self.left_tree(root.right,res)
        return res



    def right_tree(self,root,res):
        if root == None:
            res.append(None)
            return
        res.append(root.val)
        self.right_tree(root.right,res)
        self.right_tree(root.left,res)
        return res


if __name__ == "__main__":
    root = TreeNode(2)
    root.left = TreeNode(3)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.left.right.left = TreeNode(8)
    root.left.right.right = TreeNode(9)
    root.right.left = TreeNode(5)
    root.right.left.left = TreeNode(9)
    root.right.left.right = TreeNode(8)
    root.right.right = TreeNode(4)
    sloution = Solution()
    print(sloution.isSymmetric(root))