def multiply(integer_a: int, integer_b: int) -> int:
    lastDigitA: int = integer_a % 10
    lastDigitB: int = integer_b % 10
    absA: int = lastDigitA if lastDigitA >= 0 else -lastDigitA
    absB: int = lastDigitB if lastDigitB >= 0 else -lastDigitB
    return absA * absB