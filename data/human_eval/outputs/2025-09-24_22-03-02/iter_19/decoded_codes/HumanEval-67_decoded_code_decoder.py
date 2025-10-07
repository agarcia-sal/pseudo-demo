from typing import List

def fruit_distribution(s: str, n: int) -> int:
    lis: List[int] = []
    split_list = s.split(' ')
    for i in split_list:
        if i.isdigit():
            lis.append(int(i))
    total_apples_and_oranges = sum(lis)
    mango_count = n - total_apples_and_oranges
    return mango_count