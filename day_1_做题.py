class ListNode(object):
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def fanzhuandayin(self, ln):
        if ln.val is None:
            return False
        stack = []
        while ln:
            stack.insert(0, ln.val)
            ln = ln.next
        return stack


# 这题的游标没能搞清楚
class Solution1:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        # if l1 == None and l2 == None:
        #     return None
        # elif l1 == None:
        #     return l2
        # elif l2 == None:
        #     return l1
        l = ListNode(0)
        cur = l
        while l1 and l2:
            if l1.val > l2.val:
                cur.next = l2
                l2 = l2.next
            else:
                cur.next = l1
                l1 = l1.next
            cur = cur.next
            cur.next = l1 or l2
        return l.next


# node1 = ListNode(10)
# node2 = ListNode(11)
# node3 = ListNode(13)
# node1.next = node2
# node2.next = node3
#
# singleNode = ListNode(12)
#
# test = ListNode()
#
# S = Solution()
# print(S.fanzhuandayin(node1))
# print(S.fanzhuandayin(test))
# print(S.fanzhuandayin(singleNode))

l1 = ListNode(1)
l1.next = ListNode(2)
l1.next.next = ListNode(4)
print(l1.next.next.val)
l2 = ListNode(1)
l2.next = ListNode(3)
l2.next.next = ListNode(4)
S1 = Solution1()
print("*"*10)
print(S1.mergeTwoLists(l1, l2).next.next.next.next.next.val)
print("*"*10)