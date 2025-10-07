def digitSum(s):
    return sum(ord(c) if 'A' <= c <= 'Z' else 0 for c in s)