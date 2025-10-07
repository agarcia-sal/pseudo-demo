from typing import List

def exchange(list1: List[int], list2: List[int]) -> str:
    count_odd_in_list1 = sum(1 for element in list1 if element % 2 == 1)
    count_even_in_list2 = sum(1 for element in list2 if element % 2 == 0)
    return "YES" if count_even_in_list2 >= count_odd_in_list1 else "NO"