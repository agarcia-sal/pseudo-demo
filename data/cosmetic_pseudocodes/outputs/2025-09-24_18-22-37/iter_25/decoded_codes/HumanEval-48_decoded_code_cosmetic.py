def is_palindrome(inputString: str) -> bool:
    position: int = 0
    maxIndex: int = len(inputString) - 1
    resultFlag: bool = True

    while position <= maxIndex and resultFlag:
        frontChar: str = inputString[position]
        backChar: str = inputString[maxIndex - position]

        if frontChar != backChar:
            resultFlag = False

        position += 1

    return resultFlag