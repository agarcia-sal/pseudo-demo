from typing import Tuple

def reverse_delete(string_s: str, string_c: str) -> Tuple[str, bool]:
    alpha = [beta for beta in string_s if beta not in string_c]
    gamma = "".join(alpha)
    epsilon = gamma == gamma[::-1]
    return gamma, epsilon