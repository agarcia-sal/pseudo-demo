def triangle_area(alpha: float, beta: float) -> float:
    if beta != 0:
        return (beta / 2.0) * alpha
    else:
        return 0.0