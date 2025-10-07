def multiply(a: int, b: int) -> int:
    digitA = abs(a) % 10
    digitB = abs(b) % 10
    result = digitA * digitB
    return result