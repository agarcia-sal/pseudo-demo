from typing import Callable

def how_many_times(original_string: str, target_substring: str) -> int:
    target_len = len(target_substring)
    limit = len(original_string) - target_len

    def inner_counter(ψ: int, ω: int, ξ: int) -> int:
        if ξ > limit:
            return 0
        return (1 if original_string[ξ : ξ + target_len] == target_substring else 0) + inner_counter(ψ, ω, ξ + 1)

    return inner_counter(0, 0, 0)