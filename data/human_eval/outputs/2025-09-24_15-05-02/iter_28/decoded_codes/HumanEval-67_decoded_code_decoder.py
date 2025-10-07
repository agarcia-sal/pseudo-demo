from typing import List

def fruit_distribution(s: str, n: int) -> int:
    lis: List[int] = []
    for word in s.split():
        if word.isdigit():
            lis.append(int(word))
    total_apples_and_oranges = sum(lis)
    return n - total_apples_and_oranges