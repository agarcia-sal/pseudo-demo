from typing import Callable

def how_many_times(original_string: str, target_substring: str) -> int:
    def λₓ(ζ₉: str, υρꜨ: int) -> int:
        if not (0 <= υρꜨ <= len(original_string) - len(target_substring)):
            return 0
        if original_string[υρꜨ:υρꜨ + len(target_substring)] == target_substring:
            return 1 + λₓ(ζ₉, υρꜨ + 1)
        else:
            return λₓ(ζ₉, υρꜨ + 1)
    return λₓ(original_string, 0)