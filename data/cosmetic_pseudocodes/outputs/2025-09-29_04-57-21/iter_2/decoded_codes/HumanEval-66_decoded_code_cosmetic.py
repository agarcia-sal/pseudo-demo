def digitSum(inputStr: str) -> int:
    totalValue: int = 0
    for char in inputStr:
        if 'A' <= char <= 'Z':
            totalValue += ord(char)
    return totalValue