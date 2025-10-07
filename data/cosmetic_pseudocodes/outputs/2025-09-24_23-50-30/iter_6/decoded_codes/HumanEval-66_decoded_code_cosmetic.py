def digitSum(input_string: str) -> int:
    totalValue: int = 0
    indexCounter: int = 0
    lengthCounter: int = len(input_string)

    while indexCounter < lengthCounter:
        currentChar: str = input_string[indexCounter]
        if 'A' <= currentChar <= 'Z':
            totalValue += ord(currentChar)
        indexCounter += 1

    return totalValue