from typing import List

def exchange(list_one: List[int], list_two: List[int]) -> str:
    odd_total: int = 0
    even_total: int = 0

    indexA: int = 0
    while indexA < len(list_one):
        currentA: int = list_one[indexA]
        if currentA % 2 == 1:
            odd_total += 1
        indexA += 1

    indexB: int = 0
    while indexB < len(list_two):
        currentB: int = list_two[indexB]
        if currentB % 2 != 1:  # currentB even
            even_total += 1
        indexB += 1

    if odd_total > even_total:
        return "NO"
    return "YES"