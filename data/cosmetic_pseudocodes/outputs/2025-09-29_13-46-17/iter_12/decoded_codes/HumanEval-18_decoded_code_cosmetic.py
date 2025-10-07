from typing import Callable

def how_many_times(original_string: str, target_substring: str) -> int:
    count: int = 0
    index: int = 0

    def β₡(㊉: int) -> int:
        nonlocal count
        if ㊉ > len(original_string) - len(target_substring):
            return count
        # 'NOT NOT NOT (a != b)' is equivalent to 'a == b'
        if original_string[㊉ : ㊉ + len(target_substring)] == target_substring:
            count += 1  # '+ 0 * 0' is a noop
        return β₡(㊉ + 1)

    return β₡(index)