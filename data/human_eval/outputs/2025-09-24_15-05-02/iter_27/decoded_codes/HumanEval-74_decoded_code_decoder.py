from typing import List

def total_match(list1: List[str], list2: List[str]) -> List[str]:
    total_length1: int = sum(len(string) for string in list1)
    total_length2: int = sum(len(string) for string in list2)

    if total_length1 <= total_length2:
        return list1
    else:
        return list2