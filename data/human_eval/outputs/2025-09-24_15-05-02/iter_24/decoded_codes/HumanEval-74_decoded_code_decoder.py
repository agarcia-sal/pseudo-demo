from typing import List

def total_match(list1: List[str], list2: List[str]) -> List[str]:
    length_sum1 = sum(len(string) for string in list1)
    length_sum2 = sum(len(string) for string in list2)

    if length_sum1 <= length_sum2:
        return list1
    else:
        return list2