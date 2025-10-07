def digitSum(s) -> int:
    if s == "":
        return 0
    result = 0
    length = len(s)
    for i in range(length):
        char = s[i]
        if char.isupper():
            charValue = ord(char)
            result += charValue
        else:
            result += 0
    return result