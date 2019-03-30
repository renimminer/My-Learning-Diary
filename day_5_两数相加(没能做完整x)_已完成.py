# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


def ll_int(l):
    n = 0
    stack = []
    count = 0
    _str = ""
    while l:
        n += 1
        stack.append(l.val)
        l = l.next
    while count < n:
        count += 1
        _str += str(stack.pop())
    return int(_str)


# 正确代码
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        stack = []
        cc = 0
        str4 = ""
        c = 0
        _int1 = ll_int(l1)
        _int2 = ll_int(l2)
        str3 = str(_int1 + _int2)
        for i in str3:
            stack.append(i)
        n = len(str3)
        while cc < n:
            str4 += stack.pop()
            cc += 1
        n = len(str4)
        res = ListNode(0)
        cur = res
        while c < n-1:
            cur.next = ListNode(n)
            cur = cur.next
            c += 1
        curr = res
        for i in str4:
            curr.val = int(i)
            curr = curr.next
        return res


# 原代码
class Solution(object):
    def sum(self, l1, l2):
        stack1 = []
        stack2 = []
        stack3 = []
        str1 = ""
        str2 = ""
        str4 = ""
        n = 0
        count = 1
        c = 0
        cc = 1
        while l1 and l2:
            n += 1
            stack1.append(l1.val)
            stack2.append(l2.val)
            l1 = l1.next
            l2 = l2.next
        while count <= n:
            count += 1
            str1 += str(stack1.pop())
            str2 += str(stack2.pop())
        str3 = str(int(str1) + int(str2))
        for i in str3:
            stack3.append(i)
        n = len(str3)
        while cc <= n:
            str4 += stack3.pop()
            cc += 1
        n = len(str4)
        res = ListNode(0)
        cur = res
        while c < n:
            cur.next = ListNode(n)
            cur = cur.next
            c += 1
        # res = ListNode(0)
        # res.next = ListNode(0)
        # res.next.next = ListNode(0)
        curr = res
        for i in str4:
            curr.val = int(i)
            curr = curr.next
        return res


if __name__ == "__main__":
    l1 = ListNode(2)
    l2 = ListNode(4)
    l3 = ListNode(3)
    l1.next = l2
    l2.next = l3
    m1 = ListNode(5)
    m2 = ListNode(6)
    m3 = ListNode(4)
    m1.next = m2
    m2.next = m3
    solution = Solution()
    r = solution.sum(l1, m1)
    print(r.val)
    print(r.next.val)
    print(r.next.next.val)
