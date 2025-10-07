def multiply(x: int, y: int) -> int:
    a: int = x
    b: int = y
    remainderA: int = a % 10
    if remainderA < 0:
        remainderA = -remainderA
    remainderB: int = b % 10
    if remainderB < 0:
        remainderB = -remainderB
    return remainderA * remainderB