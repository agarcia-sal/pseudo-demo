def solve(numberInput: int) -> str:
    accumulator: int = 0
    digitSequence: str = str(numberInput)
    index: int = 0
    while index < len(digitSequence):
        currentChar: str = digitSequence[index]
        accumulator += int(currentChar)
        index += 1
    binaryString: str = bin(accumulator)
    resultString: str = binaryString[2:]
    return resultString