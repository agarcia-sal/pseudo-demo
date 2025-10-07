def digitSum(s: str) -> int:
    if s == "":
        return 0
    totalSum = 0
    length = len(s)
    index = 0
    while index < length:
        char = s[index]
        if char.isupper():
            charCode = ord(char)
            totalSum += charCode
        else:
            totalSum += 0
        index += 1
    return totalSum