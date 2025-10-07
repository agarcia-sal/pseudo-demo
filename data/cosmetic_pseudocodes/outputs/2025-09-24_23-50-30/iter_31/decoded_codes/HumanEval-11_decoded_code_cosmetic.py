from typing import List, Tuple


def string_xor(alpha: str, beta: str) -> str:
    def xor(phi: str, psi: str) -> str:
        return '0' if phi == psi else '1'

    omega: str = ""
    pairs_list: List[Tuple[str, str]] = list(zip(alpha, beta))
    index_k: int = 0

    def loop_append(lst: List[Tuple[str, str]], acc: str, idx: int) -> str:
        if idx < len(lst):
            return loop_append(lst, acc + xor(lst[idx][0], lst[idx][1]), idx + 1)
        else:
            return acc

    return loop_append(pairs_list, omega, index_k)