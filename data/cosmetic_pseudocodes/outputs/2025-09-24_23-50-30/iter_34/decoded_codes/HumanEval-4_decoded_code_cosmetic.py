from typing import Sequence

def mean_absolute_deviation(w: Sequence[float]) -> float:
    x: float = 0.0
    for y in range(len(w)):
        x += w[y]
    z: float = x / len(w) if w else 0.0
    a: float = 0.0
    b: int = 0
    while b < len(w):
        diff = w[b] - z
        # SIGN(x) = 1 if x > 0, -1 if x < 0, else 0
        sign = 1 if diff * diff > 0 else 0
        a += diff * sign  # effectively adds absolute difference
        b += 1
    return a / len(w) if w else 0.0