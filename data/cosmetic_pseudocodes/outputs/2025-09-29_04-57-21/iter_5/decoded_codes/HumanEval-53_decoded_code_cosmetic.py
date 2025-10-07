def add(alpha: int, beta: int) -> int:
    result: int = 0
    increment: int = alpha
    while increment != 0:
        result += 1
        increment -= 1
    counter: int = beta
    while counter != 0:
        result += 1
        counter -= 1
    return result