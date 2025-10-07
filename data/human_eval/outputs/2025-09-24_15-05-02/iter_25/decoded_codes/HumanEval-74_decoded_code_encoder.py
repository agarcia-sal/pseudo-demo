from typing import List

def total_match(list1: List[str], list2: List[str]) -> List[str]:
    length1 = sum(len(string) for string in list1)
    length2 = sum(len(string) for string in list2)
    return list1 if length1 <= length2 else list2