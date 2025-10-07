from typing import List

def fruit_distribution(string_s: str, integer_n: int) -> int:
    list_of_numbers: List[int] = [int(element) for element in string_s.split() if element.isdigit()]
    return integer_n - sum(list_of_numbers)