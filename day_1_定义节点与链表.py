# 链表及常见操作
class Node(object):
    """
    创建链表的节点类型，
    节点包括两个属性：节点值，后继指向；
    节点包括四个方法：设置（更新）节点值，获取（查看）节点值，
                      设置（更新）下一个节点，获取（查看）下一个节点
    """
    def __init__(self, val=None, _next=None):
        self.val = val
        self.next = _next

    def setval(self, val):
        self.val = val

    def getval(self):
        return self.val

    def set_next(self, node):
        self.next = node

    def get_next(self):
        return self.next


# 设定无序的链表
class UnOrderList(object):
    """
    定义了一个只有头指标，没有尾指标（默认指向None）的无序链表
    该链表只有一个头指针属性
    有五个方法：查看是否为空；添加节点；查看节点总数；遍历寻找某个节点；删除某个节点（遍历的基础上）
    """
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def add(self, nd_val):
        node = Node(nd_val)
        node.set_next(self.head)  # node.next = self.head暴力修改参数（故self.__next存在必要）
        self.head = node

    def size(self):
        current = self.head
        count = 0
        while current is not None:
            count += 1
            current = current.get_next()
        return count

    def search(self, nd_val):
        """# if current.val != nd_val:;current.val在此处不算错，
# 然而除非是传入的参数，对节点的取值还是应该使用节点类中定义好的取值方法
        """
        current = self.head
        found = False
        while current is not None and not found:  # and的后半句表示，遍历中发现了欲寻节点，便不需继续遍历下去
            if current.getval() != nd_val:
                current = current.get_next()
            else:
                found = True
                return found
        return found

    def remove(self, nd_val):
        current = self.head
        found = False
        previous = None
        while not found:
            if current.getval() == nd_val:
                found = True
            else:
                previous = current
                current = current.get_next()
        if previous is None:
            self.head = self.head.get_next()
        else:
            previous.set_next(current.get_next())  # per.get_next() = current.get_next()


if __name__ == '__main__':
    # 链表节点测试
    root = Node(1)  # 类中可以直接传递__init__的参数
    root.setval(1)
    print(root.val)
    root.getval()
    node1 = Node()
    node1.setval(2)
    root.set_next(node1)
    root.get_next()
    print(root.next.val)

    # 链表测试
    li = UnOrderList()
    print(li.is_empty())
    li.add(1)  # liadd(Node(1))画蛇添足
    li.add(2)
    li.add(3)
    print(li.head.next.get_next().val)  # 列表头节点是3，2，1
    print(li.is_empty())
    print(li.size())
    print(li.search(2))
    print(li.search(4))
    li.remove(2)
    print(li.search(2))
