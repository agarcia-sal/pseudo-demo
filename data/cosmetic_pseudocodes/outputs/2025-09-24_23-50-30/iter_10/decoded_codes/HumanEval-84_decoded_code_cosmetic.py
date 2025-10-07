def solve(numberInput: int) -> str:
    sumAccumulator = 0
    indexCounter = 0
    stringForm = str(numberInput)
    while indexCounter < len(stringForm):
        digitExtract = stringForm[indexCounter]
        digitValue = ord(digitExtract) - ord('0')
        sumAccumulator += digitValue
        indexCounter += 1
    fullBinary = bin(sumAccumulator)
    resultBinary = fullBinary[2:]
    return resultBinary