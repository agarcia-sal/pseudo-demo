def digitSum(s):
    if s == "":
        return 0
    total = 0
    for char in s:
        if char.isupper():
            total += ord(char)
    return total