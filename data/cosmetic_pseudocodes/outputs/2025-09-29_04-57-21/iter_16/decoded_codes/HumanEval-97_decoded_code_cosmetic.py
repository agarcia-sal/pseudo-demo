def multiply(integer_a: int, integer_b: int) -> int:
    leftDigit: int = integer_a % 10
    rightDigit: int = integer_b % 10
    leftAbs: int = -leftDigit if leftDigit < 0 else leftDigit
    rightAbs: int = -rightDigit if rightDigit < 0 else rightDigit
    return leftAbs * rightAbs