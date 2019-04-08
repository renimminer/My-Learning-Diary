# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# 本算法有两个while循环，遍历链表两次，时间复杂度O（n）
# 执行用时 : 64 ms, 在Remove Nth Node From End of List的Python3提交中击败了20.63% 的用户
# 内存消耗 : 13.1 MB, 在Remove Nth Node From End of List的Python3提交中击败了0.57% 的用户
class Solution:
    """
    给定一个链表，删除链表的倒数第 n 个节点，并且返回链表的头结点。

示例：

给定一个链表: 1->2->3->4->5, 和 n = 2.

当删除了倒数第二个节点后，链表变为 1->2->3->5.
    """
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        # 前两行考虑特殊情况（链表只有一个节点，减去它）
        if head.next == None:
            return None

        # 第一次遍历，得到链表长度count
        count = 0
        cur = head
        while cur != None:
            count += 1
            cur = cur.next

        # 考虑特殊情况，删除的是头结点
        if n == count:
            head = head.next
            return head
        # 遍历到要删除节点的前一个节点，进行删除操作
        cou = 1
        curr = head
        while cou < count - n:
            curr = curr.next
            cou += 1
        # 考虑特殊情况，删除的节点是尾结点
        if curr.next.next == None:
            curr.next = None
        else:
            curr.next = curr.next.next
        return head
# 改进算法，只遍历一次
# 我们通过同时移动两个指针向前来保持这个恒定的间隔，
# 直到第一个指针到达最后一个结点。此时第二个指针将指向从最后一个结点数起的第 nn 个结点。
