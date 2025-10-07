def digitSum(inputStr: str) -> int:
    totalValue: int = 0
    for symbol in inputStr:
        if not symbol.isupper():
            continue
        totalValue += ord(symbol)
    return totalValue