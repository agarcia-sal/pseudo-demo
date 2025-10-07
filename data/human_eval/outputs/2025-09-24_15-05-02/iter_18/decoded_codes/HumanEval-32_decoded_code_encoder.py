from typing import List

def poly(xs: List[float], x: float) -> float:
    return sum(coeff * (x ** i) for i, coeff in enumerate(xs))

def find_zero(xs: List[float]) -> float:
    begin: float = -1.0
    end: float = 1.0
    val_begin = poly(xs, begin)
    val_end = poly(xs, end)

    # Expand interval until a sign change is found
    while val_begin * val_end > 0:
        begin *= 2.0
        end *= 2.0
        val_begin = poly(xs, begin)
        val_end = poly(xs, end)

    # Binary search for zero with tolerance 1e-10
    while end - begin > 1e-10:
        center = (begin + end) / 2.0
        val_center = poly(xs, center)
        if val_center * val_begin > 0:
            begin = center
            val_begin = val_center
        else:
            end = center
            val_end = val_center

    return begin