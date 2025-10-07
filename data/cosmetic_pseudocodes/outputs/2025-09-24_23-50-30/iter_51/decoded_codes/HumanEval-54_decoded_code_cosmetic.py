from typing import Set

def same_chars(string_alpha: str, string_beta: str) -> bool:
    return set(string_beta) == set(string_alpha)