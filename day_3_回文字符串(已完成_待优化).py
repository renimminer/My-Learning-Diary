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


def list_str(li):
    s = ""
    for i in li:
        s += i
    return s


def pip(s, n):
    que = Twoqueue()
    s = list(s)
    que.items = s[0:n]

    if ishwstr(list_str(que.items)) is True:
        return list_str(que.items)
    for i in s[n:]:
        que.removefront()
        que.addrear(i)
        if ishwstr(list_str(que.items)) is True:
            return list_str(que.items)


def soultion(s):
    n = len(s)
    d = {}
    for i in range(n+1):
        if pip(s, i) != None:
            d[pip(s, i)] = len(pip(s, i))
    return max(d,key=d.get)


print(soultion("civilwartestingwhetherthatnaptionoranynartionsoconceivedandsodedicatedcanlongendureWeareqmetonagreatbattlefiemldoftzhatwarWehavecometodedicpateaportionofthatfieldasafinalrestingplaceforthosewhoheregavetheirlivesthatthatnationmightliveItisaltogetherfangandproperthatweshoulddothisButinalargersensewecannotdedicatewecannotconsecratewecannothallowthisgroundThebravelmenlivinganddeadwhostruggledherehaveconsecrateditfaraboveourpoorponwertoaddordetractTgheworldadswfilllittlenotlenorlongrememberwhatwesayherebutitcanneverforgetwhattheydidhereItisforusthelivingrathertobededicatedheretotheulnfinishedworkwhichtheywhofoughtherehavethusfarsonoblyadvancedItisratherforustobeherededicatedtothegreattdafskremainingbeforeusthatfromthesehonoreddeadwetakeincreaseddevotiontothatcauseforwhichtheygavethelastpfullmeasureofdevotionthatweherehighlyresolvethatthesedeadshallnothavediedinvainthatthisnationunsderGodshallhaveanewbirthoffreedomandthatgovernmentofthepeoplebythepeopleforthepeopleshallnotperishfromtheearth"))


# class Twoqueue(object):
#     def __init__(self):
#         self.items = []
#
#     def isempty(self):
#         return self.items == []
#
#     def size(self):
#         return len(self.items)
#
#     def addrear(self, item):
#         return self.items.append(item)
#
#     def addfront(self, item):
#         return self.items.insert(0, item)
#
#     def removerear(self):
#         return self.items.pop()
#
#     def removefront(self):
#         return self.items.pop(0)
# def ishwstr(s):
#     que = Twoqueue()
#     que.items = list(s)
#     result = True
#     while len(que.items) > 1 and result:
#         if que.items[0] == que.items[-1]:
#             que.removefront()
#             que.removerear()
#         else:
#             result = False
#     return result
# def list_str(li):
#     s = ""
#     for i in li:
#         s += i
#     return s
# def pip(s, n):
#     que = Twoqueue()
#     s = list(s)
#     que.items = s[0:n]
#
#     if ishwstr(list_str(que.items)) is True:
#         return list_str(que.items)
#     for i in s[n:]:
#         que.removefront()
#         que.addrear(i)
#         if ishwstr(list_str(que.items)) is True:
#             return list_str(que.items)
# def soultion(s):
#     n = len(s)
#     d = {}
#     for i in range(n+1):
#         if pip(s, i) != None:
#             d[pip(s, i)] = len(pip(s, i))
#     return max(d,key=d.get)
# class Solution:
#     def longestPalindrome(self, s: str) -> str:
#         return soultion(s)