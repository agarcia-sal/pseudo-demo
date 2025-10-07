from typing import List

def double_the_difference(list_of_numbers: List[int]) -> int:
    total: int = 0
    for element in list_of_numbers:
        if element > 0:
            if element % 2 != 0:
                if '.' not in str(element):
                    total += element * element
    return total