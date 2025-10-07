from typing import List

def exchange(list_one: List[int], list_two: List[int]) -> str:
    count_odd_in_list_one = sum(1 for element in list_one if element % 2 == 1)
    count_even_in_list_two = sum(1 for element in list_two if element % 2 == 0)
    if count_even_in_list_two >= count_odd_in_list_one:
        return "YES"
    return "NO"