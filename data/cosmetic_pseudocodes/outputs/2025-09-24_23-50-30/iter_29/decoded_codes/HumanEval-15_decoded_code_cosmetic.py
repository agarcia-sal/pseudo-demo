from typing import List

def string_sequence(integer_alpha: int) -> str:
    list_beta: List[str] = [str(integer_gamma) for integer_gamma in range(integer_alpha + 1)]
    return " ".join(list_beta)