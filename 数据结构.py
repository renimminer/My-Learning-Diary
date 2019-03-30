def main(S,T,pos):
    """
    T为非空串。若主穿S中第pos个字符之后存在与T相等的子串，则返回第一个这样的子串在S中的位置，
否则，返回0
    :param S:
    :param T:
    :param pos:
    :return:
    """
    if pos > 0:
        n = len(S)
        m = len(T)
        while pos < n-m+1:
            sub = S[pos:pos+m]
            if sub != T:
                pos += 1
            else:
                return pos
    return 0


def index(S,T,pos):
    """
    返回子串T在主串中第pos个字符之后的位置。若不存在，则函数返回值为0
    T非空，1 <= pos<= len(S)
    :param S:
    :param T:
    :param pos:
    :return:
    """

    i = pos
    j = 1
    while i <= len(S) and j <= len(T):
        if S[i] == T[j]:
            i += 1
            j += 1
        else:
            i = i-j+2
            j = 1
    if j > T[0]:
        return i-T[0]
    else:
        return 0


#print(main("azxcvbbcde","bcd",1))