from typing import List, Tuple

def sum_product(array_of_numbers: List[int]) -> Tuple[int, int]:
    alpha: int = 0
    beta: int = 1

    def recur(chars: List[int]) -> Tuple[int, int]:
        nonlocal alpha, beta
        if not chars:
            return alpha, beta
        omega = chars[0]
        alpha += omega
        beta *= omega
        return recur(chars[1:])

    return recur(array_of_numbers)