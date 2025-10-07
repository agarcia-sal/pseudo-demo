from typing import List

def fruit_distribution(s: str, n: int) -> int:
    numbers_list: List[int] = []
    for word in s.split():
        if word.isdigit():
            numbers_list.append(int(word))
    return n - sum(numbers_list)