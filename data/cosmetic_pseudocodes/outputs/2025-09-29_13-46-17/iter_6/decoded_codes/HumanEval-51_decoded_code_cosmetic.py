from typing import Callable


def remove_vowels(text: str) -> str:
    def helper_function(t: str, idx: int, result_acc: str) -> str:
        if idx >= len(t):
            return result_acc
        char_at_idx = t[idx]
        test_char = char_at_idx.lower()
        if test_char not in {"a", "e", "i", "o", "u"}:
            return helper_function(t, idx + 1, result_acc + char_at_idx)
        else:
            return helper_function(t, idx + 1, result_acc)

    return helper_function(text, 0, "")