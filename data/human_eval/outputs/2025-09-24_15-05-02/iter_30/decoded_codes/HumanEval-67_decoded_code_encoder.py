from typing import List

def fruit_distribution(s: str, n: int) -> int:
    lis: List[int] = []
    for element in s.split():
        if element.isdigit():
            lis.append(int(element))
    return n - sum(lis)