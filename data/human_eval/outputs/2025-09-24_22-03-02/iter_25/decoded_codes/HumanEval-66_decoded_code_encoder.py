def digitSum(s: str) -> int:
    if s == "":
        return 0
    totalSum = 0
    for index in range(len(s)):
        currentChar = s[index]
        if currentChar.isupper():
            asciiValue = ord(currentChar)
            totalSum += asciiValue
        else:
            totalSum += 0
    return totalSum