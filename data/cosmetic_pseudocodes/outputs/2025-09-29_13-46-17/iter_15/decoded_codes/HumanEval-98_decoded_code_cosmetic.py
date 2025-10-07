from typing import Callable

def count_upper(string_input: str) -> int:
    def λ(ι: int, ϟ: int) -> int:
        if ι >= len(string_input):
            return ϟ
        if string_input[ι] in {'A', 'E', 'I', 'O', 'U'}:
            return λ(ι + 2, ϟ + 1)
        return λ(ι + 2, ϟ)
    return λ(0, 0)