# 数组中重复的数字
def commend(list_n):
    l = []
    for i in list_n:
        if i not in l:
            l.append(i)
        else:
            return i


def offer(list_n):
    found = False
    while not found:
        for i in range(len(list_n)):
            if list_n[i] == i:                  # 首先比较这个数字（m）是不是i
                continue                        # 如果是，扫描下一个
            elif list_n[i] == list_n[list_n[i]]:  # 如果不是，看第m个位置，是不是m
                found = True                      # 如果是，返回得到的一个重复数值
                return list_n[i]
            else:                                 # 如果不是，交换两个值的位置，重新从头开始一次查询
                item = list_n[list_n[i]]
                list_n[list_n[i]] = list_n[i]
                list_n[i] = item
                print(list_n)
                break


# -*- coding:utf-8 -*-
'''
在一个二维数组中，每一行都按照从左到右递增的顺序排序
每一列都按照从上到下递增的顺序排序。
请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。
'''

'''
查找方式从右上角开始查找
如果当前元素大于target, 左移一位继续查找
如果当前元素小于target, 下移一位继续查找
进行了简单的修改, 可以判定输入类型为字符的情况
'''

'''
如果出现了array中既有字符串,又有数字,可能需要用到ord()函数,这里就不展开讨论了
'''

class Solution:
    # array 二维列表
    def Find(self, array, target):
        # 判断数组是否为空
        if array == []:
            return False

        rawnum = len(array)
        colnum = len(array[0])

        # 判断非法输入
        # 可以换成 isinstance(target, (int, float)) 进行判断
        if type(target) == float and type(array[0][0]) == int:
            if int(target) == target:
                return False
            target = int(target)
        elif type(target) == int and type(array[0][0]) == float:
            target = float(int)
        elif type(target) != type(array[0][0]):     # 浮点数的相等判断问题需要特别注意, 一般都是判断两个数的差值是否小于一个特别小的数。这里不展开分析。
            return False

        i = colnum - 1
        j = 0
        while i >= 0 and j < rawnum:
            if array[j][i] < target:
                j += 1
            elif array[j][i] > target:
                i -= 1
            else:
                return True
        return False
    # 扩展, 输出数组中target的个数
    def searchMatrix(self, matrix, target):
        if matrix == None or len(matrix) == 0:
            return 0
        rows = len(matrix)
        cols = len(matrix[0])
        row, col = 0, cols - 1
        count = 0
        while row <= rows - 1 and col >= 0:
            if matrix[row][col] > target:
                col -= 1
            elif matrix[row][col] < target:
                row += 1
            else:
                count += 1
                col -= 1
        return count


'''
请实现一个函数，将一个字符串中的空格替换成“%20”。
例如，当字符串为We Are Happy.则经过替换之后的字符串为We%20Are%20Happy。
'''


# -*- coding:utf-8 -*-
class Solution:
    # s 源字符串

    # 使用append一次遍历即可替换
    # 由于list的append是O(1)的时间复杂度，除了扩容所导致的时间损耗，该算法复杂度为O(n)
    def replaceSpaceByAppend(self, s):
        string = list(string)
        stringReplace = []
        for item in string:
            if item == ' ':
                stringReplace.append('%')
                stringReplace.append('2')
                stringReplace.append('0')
            else:
                stringReplace.append(item)
        return "".join(stringReplace)


# 创建新的字符串进行替换
def replaceSpace1(self, s):
    tempstr = ''
    if type(s) != str:
        return
    for c in s:
        if c == ' ':
            tempstr += '%20'
        else:
            tempstr += c
    return tempstr


# 简单代码替换
# 在Python中str类型是不可变的类型, 使用replace语句会生成一个新的str, 原始的s还是带空格的str变量
def replaceSpace2(self, s):
    if type(s) != str:
        return
    return s.replace(' ', '%20')


# 书中给的思路
# 判断输入类型的时候，isinstance必须首先判断，因为如果输入为integer的话，没有len，就会直接报错
def replaceSpace3(self, s):
    if not isinstance(s, str) or len(s) <= 0 or s == None:
        return ""
    spaceNum = 0
    for i in s:
        if i == " ":
            spaceNum += 1

    newStrLen = len(s) + spaceNum * 2
    newStr = newStrLen * [None]
    indexOfOriginal, indexOfNew = len(s) - 1, newStrLen - 1
    while indexOfNew >= 0 and indexOfNew >= indexOfOriginal:
        if s[indexOfOriginal] == ' ':
            newStr[indexOfNew - 2:indexOfNew + 1] = ['%', '2', '0']
            indexOfNew -= 3
            indexOfOriginal -= 1
        else:
            newStr[indexOfNew] = s[indexOfOriginal]
            indexOfNew -= 1
            indexOfOriginal -= 1
    return "".join(newStr)


if __name__ == "__main__":
    print(offer([4, 6, 1, 0, 2, 5, 3, 1]))
    array = [[1, 2, 8, 9],
             [2, 4, 9, 12],
             [4, 7, 10, 13],
             [6, 8, 11, 15]]
    array2 = []
    array3 = [['a', 'b', 'c'],
              ['b', 'c', 'd']]
    s = 'we are happy'
    test = Solution()
    print(test.replaceSpace1(s))
    print(test.replaceSpace2(s))
    print(test.replaceSpace3(s))