from typing import List

def circular_shift(integer_alpha: int, integer_beta: int) -> str:
    list_gamma: List[str] = list(str(integer_alpha))
    if not (integer_beta <= len(list_gamma)):
        return ''.join(reversed(list_gamma))
    else:
        list_delta: List[str] = list_gamma[len(list_gamma) - integer_beta : len(list_gamma)]
        list_epsilon: List[str] = list_gamma[0 : len(list_gamma) - integer_beta]
        return ''.join(list_delta + list_epsilon)