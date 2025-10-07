from typing import Callable

def how_many_times(original_string: str, target_substring: str) -> int:
    def α1(ι: int, ω: int, τ: int) -> int:
        if ι < (ω - τ + 1):
            if original_string[ι:ι + τ] != target_substring:
                return α1(ι + 1, ω, τ)
            else:
                return 1 + α1(ι + 1, ω, τ)
        else:
            return 0
    return α1(0, len(original_string), len(target_substring))