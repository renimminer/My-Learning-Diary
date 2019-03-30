# 1、去空格及特殊符号
s.strip().lstrip().rstrip(',')

# >>> str = ' ab cd '
# # >>> str
# # ' ab cd '
# # >>> str.strip() #删除头尾空格(包括\n、\r、\t、' '，即：换行、回车、制表符、空格)
# # 'ab cd'
# # >>> str.lstrip() #删除开头空格(包括\n、\r、\t、' '，即：换行、回车、制表符、空格)
# # 'ab cd '
# # >>> str.rstrip() #删除结尾空格(包括\n、\r、\t、' '，即：换行、回车、制表符、空格)
# # ' ab cd'

# >>> str2 = '1a2b12c21'
# >>> str2.strip('12') #删除头尾的1和2
# 'a2b12c'
# >>> str2.lstrip('12') #删除开头的1和2
# 'a2b12c21'
# >>> str2.rstrip('12') #删除结尾的1和2
# '1a2b12c'

# 6、扫描字符串是否包含指定的字符
sStr1 = '12345678'
sStr2 = '456'
print(len(sStr1 and sStr2))

# 8、将字符串中的大小写转换
S.lower()  # 小写
S.upper()  # 大写
S.swapcase()  # 大小写互换
S.capitalize()  # 首字母大写
String.capwords(S)  # 这是模块中的方法。它把S用split()函数分开，然后用capitalize()把首字母变成大写，最后用join()合并到一起


# 9、追加指定长度的字符串
sStr1 = '12345'
sStr2 = 'abcdef'
n = 3
sStr1 += sStr2[0:n]
print(sStr1)

# 11、复制指定长度的字符
sStr1 = ''
sStr2 = '12345'
n = 3
sStr1 = sStr2[0:n]
print(sStr1)

# 12、将字符串前n个字符替换为指定的字符
sStr1 = '12345'
ch = 'r'
n = 3
sStr1 = n * ch + sStr1[3:]
print(sStr1)

# 13、扫描字符串
sStr1 = 'cekjgdklab'
sStr2 = 'gka'
nPos = -1
for c in sStr1:
    if c in sStr2:
        nPos = sStr1.index(c)
        break
print(nPos)


# 14、翻转字符串
sStr1 = 'abcdefg'
sStr1 = sStr1[::-1]
print(sStr1)

15、查找字符串
sStr1 = 'abcdefg'
sStr2 = 'cde'
print(sStr1.find(sStr2))

# 16、分割字符串
sStr1 = 'ab,cde,fgh,ijk'
sStr2 = ','
sStr1 = sStr1[sStr1.find(sStr2) + 1:]
print(sStr1)
# # 或者
s = 'ab,cde,fgh,ijk'
print(s.split(','))

# 17、连接字符串
delimiter = ','
mylist = ['Brazil', 'Russia', 'India', 'China']
print(delimiter.join(mylist))


# 18、PHP中addslashes的实现
s = "John 'Johny' Doe (a.k.a. \"Super Joe\")\\\0"
def addslashes(s):
    d = {'"': '\\"', "'": "\\'", "\0": "\\\0", "\\": "\\\\"}
    return ''.join(d.get(c, c) for c in s)   # Python 字典(Dictionary) get() 函数返回指定键的值，
                                                            # 如果值不在字典中返回默认值。
print(s)
print(addslashes(s))

# 19、只显示字母与数字
def OnlyCharNum(s, oth=''):
    s2 = s.lower();
    fomart = 'abcdefghijklmnopqrstuvwxyz0123456789'
    for c in s2:
        if not c in fomart:
            s = s.replace(c, '');
    return s;
print(OnlyCharNum("a000 aa-b"))

# 20、截取字符串
str1 = "0123456789"
print(str1[0:3])  # 截取第一位到第三位的字符
print(str1[:])  # 截取字符串的全部字符
print(str1[6:])  # 截取第七个字符到结尾
print(str1[:-3])  # 截取从头开始到倒数第三个字符之前
print(str1[2])  # 截取第三个字符
print(str1[-1])  # 截取倒数第一个字符
print(str1[::-1])  # 创造一个与原字符串顺序相反的字符串
print(str1[-3:-1])  # 截取倒数第三位与倒数第一位之前的字符
print(str1[-3:])  # 截取倒数第三位到结尾
print(str1[:-5:-3])  # 逆序截取，具体啥意思没搞明白？

# 21、字符串在输出时的对齐
S.ljust(width, [fillchar])
# 输出width个字符，S左对齐，不足部分用fillchar填充，默认的为空格。
S.rjust(width, [fillchar])  # 右对齐
S.center(width, [fillchar])  # 中间对齐
S.zfill(width)  # 把S变成width长，并在右对齐，不足部分用0补足
#  1 >>> str = "this is string example....wow!!!";
#  2 >>> str.ljust(50,'0')
#  3 'this is string example....wow!!!000000000000000000'
#  4 >>> str.ljust(50)
#  5 'this is string example....wow!!!                  '
#  6 >>> str.rjust(50)
#  7 '                  this is string example....wow!!!'
#  8 >>> str.rjust(50,'0')
#  9 '000000000000000000this is string example....wow!!!'
# 10 >>> str.center(50,'0')
# 11 '000000000this is string example....wow!!!000000000'
# 12 >>> str.center(50)
# 13 '         this is string example....wow!!!         '
# 14 >>> str.zfill(50)
# 15 '000000000000000000this is string example....wow!!!'

# 22、字符串中的搜索和替换
S.find(substr, [start, [end]])
# 返回S中出现substr的第一个字母的标号，如果S中没有substr则返回-1。start和end作用就相当于在S[start:end]中搜索
S.index(substr, [start, [end]])
# 与find()相同，只是在S中没有substr时，会返回一个运行时错误
S.rfind(substr, [start, [end]])
# 返回S中最后出现的substr的第一个字母的标号，如果S中没有substr则返回-1，也就是说从右边算起的第一次出现的substr的首字母标号
S.rindex(substr, [start, [end]])
S.count(substr, [start, [end]])  # 计算substr在S中出现的次数
S.replace(oldstr, newstr, [count])
# 把S中的oldstar替换为newstr，count为替换次数。这是替换的通用形式，还有一些函数进行特殊字符的替换
S.strip([chars])
# 把S中前后chars中有的字符全部去掉，可以理解为把S前后chars替换为None
S.lstrip([chars])
S.rstrip([chars])
S.expandtabs([tabsize])
# 把S中的tab字符替换没空格，每个tab替换为tabsize个空格，默认是8个

# 23、字符串的分割和组合
S.split([sep, [maxsplit]])
# 以sep为分隔符，把S分成一个list。maxsplit表示分割的次数。默认的分割符为空白字符
S.rsplit([sep, [maxsplit]])
S.splitlines([keepends])
# 把S按照行分割符分为一个list，keepends是一个bool值，如果为真每行后而会保留行分割符。
S.join(seq)  # 把seq代表的序列──字符串序列，用S连接起来


# 25、字符串还有一对编码和解码的函数
S.encode([encoding, [errors]])
# 其中encoding可以有多种值，比如gb2312 gbk gb18030 bz2 zlib big5 bzse64等都支持。errors默认值为"strict"，意思是UnicodeError。可能的值还有'ignore', 'replace', 'xmlcharrefreplace', 'backslashreplace' 和所有的通过codecs.register_error注册的值。这一部分内容涉及codecs模块，不是特明白
S.decode([encoding, [errors]])


S.isalnum()
# 是否全是字母和数字，并至少有一个字符
S.isalpha()  # 是否全是字母，并至少有一个字符
S.isdigit()  # 是否全是数字，并至少有一个字符
S.isspace()  # 是否全是空白字符，并至少有一个字符
S.islower()  # S中的字母是否全是小写
S.isupper()  # S中的字母是否便是大写
S.istitle()  # S是否是首字母大写的

