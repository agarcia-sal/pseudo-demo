def multiply(integer_a: int, integer_b: int) -> int:
    remainderA = integer_a - (integer_a // 10) * 10
    remainderB = integer_b - (integer_b // 10) * 10
    if remainderA < 0:
        remainderA = -remainderA
    if remainderB < 0:
        remainderB = -remainderB
    return remainderA * remainderB