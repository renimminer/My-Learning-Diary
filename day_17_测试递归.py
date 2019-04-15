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
        if root.left.val == root.right.val and self.isSymmetric(root.left) == self.isSymmetric(root.right):
            return True
        else:
            return False

class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if p == None and q == None:
            return True
        elif p == None or q == None:
            return False
        p_queue = self.queue_(p,[])
        q_queue = self.queue_(q,[])
        for i, j in zip(p_queue, q_queue):
            if i != j:
                return False
        return True


    def queue_(self,p,queue):
        if p is None:
            return
        self.queue_(p.left,queue)
        queue.append(p.val)
        self.queue_(p.right,queue)
        return queue

if __name__ == "__main__":
    p = TreeNode(1)
    p.left = TreeNode(2)
    #p.right = TreeNode(3)
    q = TreeNode(1)
    q.left = None#TreeNode(2)
    q.right = TreeNode(2)
    solution = Solution()
    print(solution.isSameTree(p,q))
