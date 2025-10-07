def digitSum(s: str) -> int:
    if s == "":
        return 0
    totalSum = 0
    for char in s:
        if char.isupper():
            charValue = ord(char)
        else:
            charValue = 0
        totalSum += charValue
    return totalSum