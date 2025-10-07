def reverse_delete(s, c):
    res = ''.join(ch for ch in s if ch not in c)
    return res, res == res[::-1]