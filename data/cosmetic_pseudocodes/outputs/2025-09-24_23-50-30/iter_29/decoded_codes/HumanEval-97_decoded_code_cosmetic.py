def multiply(alpha: int, beta: int) -> int:
    x: int = alpha % 10
    y: int = beta % 10
    return (abs(x)) * (abs(y))