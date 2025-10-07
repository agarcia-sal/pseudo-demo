def multiply(x: int, y: int) -> int:
    lastDigitX = x % 10
    lastDigitY = y % 10
    posX = -lastDigitX if lastDigitX < 0 else lastDigitX
    posY = -lastDigitY if lastDigitY < 0 else lastDigitY
    return posX * posY