class Solution:
    def convert(self, s, m):
        n = len(s)  # 字符串长度为n
        a = s // 2m-2  # 取整为a，即整除了a次
        b = s % 2m-2  # 取于为b，b < 2m-2
        # 构造一个列表li，它有m个元素。列表中，第m个元素是第m行字符加总。目前只有每个元素只有第一个字符
        li = [i for i in range(m)]
        i = 0
        while i < m:
            li[i] = s[i]
            i += 1
