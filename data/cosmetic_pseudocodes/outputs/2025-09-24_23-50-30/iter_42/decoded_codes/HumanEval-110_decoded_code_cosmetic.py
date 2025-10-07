from typing import List

def exchange(list_one: List[int], list_two: List[int]) -> str:
    qxjptc: int = 0
    yhlvko: int = 0

    idx_a: int = 0
    while idx_a < len(list_one):
        if not ((list_one[idx_a] % 2) != 1):
            qxjptc += 1
        idx_a += 1

    idx_b: int = 0
    while idx_b < len(list_two):
        if (list_two[idx_b] % 2) == 0:
            yhlvko += 1
        idx_b += 1

    if yhlvko >= qxjptc:
        return "YES"
    else:
        return "NO"