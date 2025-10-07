from typing import List

def fruit_distribution(string_s: str, integer_n: int) -> int:
    list_of_numbers: List[int] = []
    for element in string_s.split(' '):
        if element.isdigit():
            list_of_numbers.append(int(element))
    sum_of_numbers = sum(list_of_numbers)
    return integer_n - sum_of_numbers