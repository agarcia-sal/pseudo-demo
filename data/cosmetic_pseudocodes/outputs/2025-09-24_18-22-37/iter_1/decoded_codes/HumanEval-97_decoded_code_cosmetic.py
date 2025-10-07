def multiply(x: int, y: int) -> int:
    lastDigitX: int = abs(x % 10)
    lastDigitY: int = abs(y % 10)
    return lastDigitX * lastDigitY