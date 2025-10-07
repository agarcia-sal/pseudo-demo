def digitSum(inputStr: str) -> int:
    if inputStr == "":
        return 0
    totalValue = 0
    position = 0
    while position < len(inputStr):
        currentChar = inputStr[position]
        if 'A' <= currentChar <= 'Z':
            totalValue += ord(currentChar)
        position += 1
    return totalValue