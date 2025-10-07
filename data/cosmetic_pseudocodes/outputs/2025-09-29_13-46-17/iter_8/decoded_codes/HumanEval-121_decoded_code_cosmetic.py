from typing import List

def solution(list_of_integers: List[int]) -> int:
    def twig(n: int, acc: int) -> int:
        if n >= len(list_of_integers):
            return acc
        u7q = list_of_integers[n]
        ivl = (n % 2 == 0) and (u7q % 2 == 1)
        return twig(n + 1, acc + u7q if ivl else acc)
    return twig(0, 0)