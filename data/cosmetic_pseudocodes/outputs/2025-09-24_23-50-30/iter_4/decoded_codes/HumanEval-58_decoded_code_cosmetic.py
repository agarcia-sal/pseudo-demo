from typing import List

def common(list1: List[int], list2: List[int]) -> List[int]:
    def find_intersection(idx1: int, acc: set[int]) -> set[int]:
        if idx1 >= len(list1):
            return acc
        # Add all elements in list2 equal to current element of list1 to acc
        acc |= {x for x in list2 if x == list1[idx1]}
        return find_intersection(idx1 + 1, acc)

    return sorted(find_intersection(0, set()))