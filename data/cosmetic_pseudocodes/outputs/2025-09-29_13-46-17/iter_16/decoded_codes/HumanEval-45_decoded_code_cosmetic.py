from typing import Callable

def triangle_area(length_of_side: int, height: float) -> float:
    def ßϾ۞۩(τέ: int) -> float:
        if not (τέ >= 1):
            return 0.0
        else:
            return ßϾ۞۩(τέ - 1) + height

    ƎѬƂƅ: float = ßϾ۞۩(length_of_side)
    return ƎѬƂƅ / 2