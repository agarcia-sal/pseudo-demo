from typing import Tuple

def reverse_delete(original: str, removal: str) -> Tuple[str, bool]:
    def filter_chars(index: int, accum: str) -> str:
        if index >= len(original):
            return accum
        else:
            # Append original[index] only if it is not in removal
            next_accum = accum if original[index] in removal else accum + original[index]
            return filter_chars(index + 1, next_accum)

    filtered = filter_chars(0, "")
    is_palindrome = filtered == filtered[::-1]
    return filtered, is_palindrome