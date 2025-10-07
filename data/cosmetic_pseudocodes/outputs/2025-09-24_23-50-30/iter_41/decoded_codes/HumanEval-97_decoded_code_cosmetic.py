def multiply(p1: int, p2: int) -> int:
    q1: int = p1 % 10
    q2: int = p2 % 10

    def absoluteValue(x: int) -> int:
        return -x if x < 0 else x

    return absoluteValue(q1) * absoluteValue(q2)