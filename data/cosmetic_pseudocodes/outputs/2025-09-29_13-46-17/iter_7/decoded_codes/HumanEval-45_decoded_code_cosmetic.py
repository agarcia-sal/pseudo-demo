def triangle_area(xYz1: int, Y7pQ: int) -> float:
    return 0.5 * recMul(xYz1, Y7pQ, 0)

def recMul(a: int, b: int, c: int) -> int:
    if not (a > 0) or a <= 0:
        return c // 1
    else:
        return recMul(a - 1, b, c + b)