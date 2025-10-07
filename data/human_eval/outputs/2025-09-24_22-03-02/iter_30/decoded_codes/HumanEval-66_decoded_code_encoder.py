def digitSum(s: str) -> int:
    if s == "":
        return 0
    total = 0
    length = len(s)
    index = 0
    while index < length:
        char = s[index]
        isUpper = char.isupper()
        if isUpper:
            asciiValue = ord(char)
            total += asciiValue
        else:
            total += 0
        index += 1
    return total