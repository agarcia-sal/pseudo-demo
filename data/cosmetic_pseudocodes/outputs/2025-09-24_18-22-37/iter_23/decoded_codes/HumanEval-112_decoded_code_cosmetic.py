from typing import Tuple

def reverse_delete(string_alpha: str, string_beta: str) -> Tuple[str, bool]:
    string_gamma = ''.join(char for char in string_alpha if char not in string_beta)
    boolean_delta = string_gamma == string_gamma[::-1]
    return string_gamma, boolean_delta