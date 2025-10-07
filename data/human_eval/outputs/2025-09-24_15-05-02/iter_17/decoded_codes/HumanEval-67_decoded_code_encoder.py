from typing import List

def fruit_distribution(s: str, n: int) -> int:
    lis: List[int] = []
    for i in s.split(' '):
        if i.isdigit():
            lis.append(int(i))
    total_apples_and_oranges: int = sum(lis)
    return n - total_apples_and_oranges