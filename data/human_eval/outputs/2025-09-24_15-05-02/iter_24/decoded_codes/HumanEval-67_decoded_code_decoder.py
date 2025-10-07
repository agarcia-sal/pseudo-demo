from typing import List

def fruit_distribution(string_s: str, integer_n: int) -> int:
    numbers_list: List[int] = [int(word) for word in string_s.split() if word.isdigit()]
    total_apples_and_oranges: int = sum(numbers_list)
    return integer_n - total_apples_and_oranges