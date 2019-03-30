# 给定二叉搜索树的根结点 root，返回 L 和 R（含）之间的所有结点的值的和。

# 二叉搜索树保证具有唯一的值
class TreeNode():
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right

class Solution:
    def rangeSumBST(self, root, L, R):
        if root == None:
            return 0
        list_root = self.pro_order(root)
        if None in list_root:
            list_root.remove(None)
        li = []
        for i in list_root:
            if L <= i <= R:
                li.append(i)
        return sum(li)

    def pro_order(self,root):
        if root == None:
            return False
        list_root.append(root.val)
        self.pro_order(root.left)
        self.pro_order(root.right)
        return list_root



list_root = []
# root = TreeNode(10,TreeNode(5,TreeNode(3),TreeNode(7)),TreeNode(15,TreeNode(None),TreeNode(18)))
root = TreeNode(10,TreeNode(5,TreeNode(3,TreeNode(1),TreeNode(None)),TreeNode(7,TreeNode(6))),TreeNode(15,TreeNode(13),TreeNode(18)))
solution = Solution()
#print(solution.rangeSumBST(root,7,15))
print(solution.rangeSumBST(root,6,10))
print(solution.pro_order(root))