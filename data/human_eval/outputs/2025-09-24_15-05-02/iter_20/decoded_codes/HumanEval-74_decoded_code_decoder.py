from typing import List

def total_match(list1: List[str], list2: List[str]) -> List[str]:
    length1: int = 0
    for string in list1:
        length1 += len(string)

    length2: int = 0
    for string in list2:
        length2 += len(string)

    if length1 <= length2:
        return list1
    else:
        return list2