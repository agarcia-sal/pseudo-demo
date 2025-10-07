def digitSum(s) -> int:
    if s == "":
        return 0
    total = 0
    length = len(s)
    index = 0
    while index < length:
        char = s[index]
        if char.isupper():
            asciiValue = ord(char)
            total += asciiValue
        else:
            total += 0
        index += 1
    return total