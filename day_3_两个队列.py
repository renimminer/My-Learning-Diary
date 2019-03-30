class Queue(object):
    """
    构造一个单向队列，属性只有一个队列列表，
    方法有四个，是否空队列；队列长度；左端添加；右端删除
    """
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        return self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop()

    def isempty(self):
        return self.items == []

    def size(self):
        return len(self.items)


class Twoqueue(object):
    """
    创建一个两侧都能进行添加与删除操作的队列
    它有一个属性，定义为可查看
    有六个方法，是否为空；长度大小；尾部添加；首部添加；尾部删除；首部删除
    """
    def __init__(self):
        self.items = []

    def isempty(self):
        return self.items == []

    def size(self):
        return len(self.items)

    def addrear(self, item):
        return self.items.append(item)

    def addfront(self, item):
        return self.items.insert(0, item)

    def removerear(self):
        return self.items.pop()

    def removefront(self):
        return self.items.pop(0)


def ishwstr(s):
    """
    判断给定的字符串是否是回文字符串
    :param s: str
    :return: True or False
    """
    que = Twoqueue()
    que.items = list(s)
    result = True
    while len(que.items) > 1 and result:
        if que.items[0] == que.items[-1]:
            que.removefront()
            que.removerear()
        else:
            result = False
    return result


if __name__ == "__main__":
    # 单项队列测试
    # queue = Queue()
    # print(queue.isempty())
    # print(queue.size())
    # queue.enqueue(1)
    # queue.enqueue(2)
    # print(queue.size())
    # queue.dequeue()
    # print(queue.size())

    # 测试双向队列
    # tq = Twoqueue()
    # print(tq.isempty())
    # tq.addfront(2)
    # tq.addrear(3)
    # tq.addfront(1)
    # print(tq.isempty())
    # print(tq.size())
    # print(tq.items)
    # tq.removefront()
    # tq.removerear()
    # print(tq.items)

    # 测试回文字符串函数
    print(ishwstr("bb"))



