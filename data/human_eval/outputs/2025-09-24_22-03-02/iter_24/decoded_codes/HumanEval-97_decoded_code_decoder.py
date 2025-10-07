def multiply(a: int, b: int) -> int:
    remainderA = a % 10
    if remainderA < 0:
        remainderA = -remainderA
    remainderB = b % 10
    if remainderB < 0:
        remainderB = -remainderB
    product = remainderA * remainderB
    return product