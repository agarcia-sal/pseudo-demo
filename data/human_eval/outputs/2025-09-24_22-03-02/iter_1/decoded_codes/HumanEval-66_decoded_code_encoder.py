def digitSum(s):
    if not s:
        return 0
    return sum(ord(c) for c in s if c.isupper())