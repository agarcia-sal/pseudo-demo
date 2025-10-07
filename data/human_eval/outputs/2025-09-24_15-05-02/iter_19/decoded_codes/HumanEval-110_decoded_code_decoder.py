from typing import List

def exchange(list1: List[int], list2: List[int]) -> str:
    count_odd_in_list1: int = sum(1 for element in list1 if element % 2 == 1)
    count_even_in_list2: int = sum(1 for element in list2 if element % 2 == 0)

    if count_even_in_list2 >= count_odd_in_list1:
        return "YES"
    else:
        return "NO"