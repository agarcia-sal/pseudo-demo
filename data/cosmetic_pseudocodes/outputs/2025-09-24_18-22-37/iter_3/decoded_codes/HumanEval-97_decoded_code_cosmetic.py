def multiply(integer_a: int, integer_b: int) -> int:
    digitA: int = integer_a
    digitB: int = integer_b

    if digitA < 0:
        digitA = -digitA

    if digitB < 0:
        digitB = -digitB

    lastDigitA: int = digitA - ((digitA // 10) * 10)
    lastDigitB: int = digitB - ((digitB // 10) * 10)
    result: int = 0

    while lastDigitA > 0:
        result += lastDigitB
        lastDigitA -= 1

    return result