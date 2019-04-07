# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    """
    反转一个单链表。

示例:

输入: 1->2->3->4->5->NULL
输出: 5->4->3->2->1->NULL
    """
    def reverseList(self, head: ListNode) -> ListNode:
        if head == None:
            return head
        else:
            cur = head
            stack = []
            while cur:
                stack.append(cur)
                cur = cur.next
            re = stack.pop()
            he = re
            while stack != []:
                he.next = stack.pop()
                he = he.next
            he.next = None
            return re


#  优秀范例


class Solution:
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return head
        last = None
        while head:
            tmp = head.next
            head.next = last
            last = head
            head = tmp
        return last