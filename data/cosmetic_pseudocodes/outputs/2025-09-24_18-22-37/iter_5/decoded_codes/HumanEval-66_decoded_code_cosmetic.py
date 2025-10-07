def digitSum(inputString: str) -> int:
    totalSum: int = 0
    if len(inputString) == 0:
        return 0
    for index in range(1, len(inputString) + 1):
        currentChar: str = inputString[index - 1]
        if 'A' <= currentChar <= 'Z':
            totalSum += ord(currentChar)
    return totalSum