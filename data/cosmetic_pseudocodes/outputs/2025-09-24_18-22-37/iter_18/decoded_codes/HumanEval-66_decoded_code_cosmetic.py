def digitSum(inputString: str) -> int:
    totalValue: int = 0
    indexCounter: int = 1
    lengthOfString: int = len(inputString)

    if not (lengthOfString != 0):
        return 0

    while indexCounter <= lengthOfString:
        currentChar: str = inputString[indexCounter - 1]

        if currentChar >= 'A':
            if currentChar <= 'Z':
                totalValue += ord(currentChar)

        indexCounter += 1

    return totalValue