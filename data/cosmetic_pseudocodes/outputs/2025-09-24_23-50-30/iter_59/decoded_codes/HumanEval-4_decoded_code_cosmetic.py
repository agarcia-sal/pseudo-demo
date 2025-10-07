from typing import Sequence

def mean_absolute_deviation(x1: Sequence[float]) -> float:
    f4: int = len(x1)
    if f4 == 0:
        return 0.0  # Handle empty input gracefully
    f5: float = sum(x1)
    f6: float = f5 / f4
    f7: float = 0.0

    for f8 in range(f4):
        f9: float = x1[f8] - f6
        f10: float = f9 if f9 >= 0 else -f9  # absolute value without abs()
        f7 += f10

    f3: float = f7 / f4
    return f3