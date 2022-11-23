def strings_xor(s, t):
    """
        s and t are string that only conatins 0 and 1 characters
    """
    res = ""
    for i in range(len(s)):
        if s[i] == t[i]:
            res += '0'
        else:
            res += '1'

    return res
