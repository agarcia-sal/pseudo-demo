def multiply(a: int, b: int) -> int:
    remainderA = a % 10
    if remainderA < 0:
        remainderA *= -1
    remainderB = b % 10
    if remainderB < 0:
        remainderB *= -1
    result = remainderA * remainderB
    return result