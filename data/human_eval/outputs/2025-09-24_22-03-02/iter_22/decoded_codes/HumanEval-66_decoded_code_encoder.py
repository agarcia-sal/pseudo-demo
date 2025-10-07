def digitSum(s: str) -> int:
    if s == "":
        return 0
    total = 0
    length = len(s)
    index = 0
    while index < length:
        char = s[index]
        if char.isupper():
            charValue = ord(char)
        else:
            charValue = 0
        total += charValue
        index += 1
    return total