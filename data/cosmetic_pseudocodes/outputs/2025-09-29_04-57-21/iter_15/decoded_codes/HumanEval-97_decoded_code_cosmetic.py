def multiply(integer_a: int, integer_b: int) -> int:
    lastDigitA = integer_a - (integer_a // 10) * 10
    if lastDigitA < 0:
        lastDigitA = -lastDigitA

    lastDigitB = integer_b - (integer_b // 10) * 10
    if lastDigitB < 0:
        lastDigitB = -lastDigitB

    return lastDigitA * lastDigitB