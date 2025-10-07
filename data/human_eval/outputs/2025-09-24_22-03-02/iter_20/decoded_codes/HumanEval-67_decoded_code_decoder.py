from typing import List

def fruit_distribution(s: str, n: int) -> int:
    lis: List[int] = []
    split_list = s.split(" ")
    for current_element in split_list:
        if current_element.isdigit():
            lis.append(int(current_element))
    total_sum = sum(lis)
    return n - total_sum