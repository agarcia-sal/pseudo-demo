from typing import List

def total_match(list_one: List[str], list_two: List[str]) -> List[str]:
    total_first: int = 0
    index_alpha: int = 0
    while index_alpha < len(list_one):
        current_letter: str = list_one[index_alpha]
        total_first += len(current_letter)
        index_alpha += 1

    total_second: int = 0
    index_beta: int = 0
    while index_beta < len(list_two):
        current_char: str = list_two[index_beta]
        total_second += len(current_char)
        index_beta += 1

    if total_first <= total_second:
        return list_one
    else:
        return list_two