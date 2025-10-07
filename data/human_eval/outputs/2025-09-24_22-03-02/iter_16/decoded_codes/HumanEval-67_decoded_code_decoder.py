from typing import List

def fruit_distribution(s: str, n: int) -> int:
    lis: List[int] = []
    for i in s.split(' '):
        if i.isdigit():
            lis.append(int(i))
    total_apples_and_oranges = 0
    for number in lis:
        total_apples_and_oranges += number
    mango_fruits = n - total_apples_and_oranges
    return mango_fruits