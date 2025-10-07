from typing import List

def fruit_distribution(s: str, n: int) -> int:
    numbers_list: List[int] = []
    for word in s.split():
        if word.isdigit():
            numbers_list.append(int(word))
    total_apples_and_oranges: int = sum(numbers_list)
    return n - total_apples_and_oranges