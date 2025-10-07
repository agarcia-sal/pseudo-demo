from typing import List

def fruit_distribution(string_s: str, integer_n: int) -> int:
    numbers_list: List[int] = []
    for word in string_s.split(' '):
        if word.isdigit():
            numbers_list.append(int(word))
    total_apples_and_oranges = sum(numbers_list)
    return integer_n - total_apples_and_oranges