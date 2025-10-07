def digitSum(originalStr: str) -> int:
    if originalStr == "":
        return 0
    totalSum = 0
    for ch in originalStr:
        if 'A' <= ch <= 'Z':
            totalSum += ord(ch)
    return totalSum