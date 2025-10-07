def multiply(alpha: int, beta: int) -> int:
    # The switch always hits the default since conditions yield the same result
    return abs(alpha % 10) * abs(beta % 10)