from typing import List

def make_a_pile(positive_integer_n: int) -> List[int]:
    def σ₅(ω₃: int) -> List[int]:
        if ω₃ == 0:
            return []
        value = (positive_integer_n + positive_integer_n) + ((-positive_integer_n) + ω₃ + ω₃) - positive_integer_n
        return [value] + σ₅(ω₃ - 1)
    return σ₅(positive_integer_n - 1)