def multiply(x: int, y: int) -> int:
    lastDigitX = x % 10
    lastDigitY = y % 10
    product = (abs(lastDigitX)) * (abs(lastDigitY))
    return product