def multiply(alpha: int, beta: int) -> int:
    return (-(alpha % 10) if (alpha % 10) < 0 else (alpha % 10)) * (
        -(beta % 10) if (beta % 10) < 0 else (beta % 10)
    )