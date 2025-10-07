from typing import List

def fruit_distribution(s: str, n: int) -> int:
    list_of_numbers: List[int] = []
    for word in s.split():
        if word.isdigit():
            list_of_numbers.append(int(word))
    return n - sum(list_of_numbers)