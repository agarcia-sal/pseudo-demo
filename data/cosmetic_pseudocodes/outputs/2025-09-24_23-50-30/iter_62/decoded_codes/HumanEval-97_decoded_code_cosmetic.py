def multiply(alpha: int, beta: int) -> int:
    def recur(x: int, y: int) -> int:
        # If either x or y is nonzero, return product of their absolute values
        if x != 0 or y != 0:
            return (abs(x) * abs(y))
        else:
            return 0

    delta: int = recur(alpha - (alpha // 10) * 10, beta - (beta // 10) * 10)
    return delta