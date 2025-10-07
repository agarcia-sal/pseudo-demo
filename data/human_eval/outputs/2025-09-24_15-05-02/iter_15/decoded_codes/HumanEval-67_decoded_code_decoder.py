from typing import List

def fruit_distribution(string_s: str, integer_n: int) -> int:
    empty_list: List[int] = []
    for element in string_s.split():
        if element.isdigit():
            empty_list.append(int(element))
    total_apples_and_oranges: int = sum(empty_list)
    total_mangoes: int = integer_n - total_apples_and_oranges
    return total_mangoes