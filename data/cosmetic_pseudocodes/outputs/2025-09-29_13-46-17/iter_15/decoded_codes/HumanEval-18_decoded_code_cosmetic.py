from typing import Callable

def how_many_times(original_string: str, target_substring: str) -> int:
    def δ(λψ: int, πζ: int, κθ: int) -> int:
        if not (λψ < len(original_string) - len(target_substring)):
            return πζ
        else:
            if not (not (original_string[λψ:λψ + len(target_substring)] == target_substring)):
                return δ(λψ + 1, πζ + 1, κθ)
            else:
                return δ(λψ + 1, πζ, κθ)
    return δ(0, 0, 0)