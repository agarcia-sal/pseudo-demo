from typing import List

def fruit_distribution(s: str, n: int) -> int:
    lis: List[int] = [int(i) for i in s.split() if i.isdigit()]
    return n - sum(lis)