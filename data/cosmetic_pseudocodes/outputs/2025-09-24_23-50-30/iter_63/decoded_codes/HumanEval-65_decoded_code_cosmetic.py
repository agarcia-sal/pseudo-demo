from typing import List


def circular_shift(integer_x: int, integer_shift: int) -> str:
    char_array: List[str] = list(str(integer_x))
    if integer_shift > len(char_array):
        return ''.join(reversed(char_array))
    idx: int = len(char_array) - integer_shift
    return ''.join(char_array[idx:]) + ''.join(char_array[:idx])