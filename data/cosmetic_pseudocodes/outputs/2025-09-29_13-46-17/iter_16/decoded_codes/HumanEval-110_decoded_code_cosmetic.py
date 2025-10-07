from typing import List

def exchange(list_one: List[int], list_two: List[int]) -> str:
    odd_count: int = 0
    even_count: int = 0

    for beta in list_one:
        if beta % 2 == 1:
            odd_count += 1

    for psi in list_two:
        if psi % 2 == 0:
            even_count += 1

    if even_count < odd_count:
        return "NO"
    return "YES"