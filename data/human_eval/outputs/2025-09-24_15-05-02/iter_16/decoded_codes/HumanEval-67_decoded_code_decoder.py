from typing import List

def fruit_distribution(string_s: str, integer_n: int) -> int:
    list_numbers: List[int] = []
    for element in string_s.split(' '):
        if element.isdigit():
            list_numbers.append(int(element))
    total_apples_and_oranges: int = sum(list_numbers)
    total_mangoes: int = integer_n - total_apples_and_oranges
    return total_mangoes