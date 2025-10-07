from typing import List

def pairs_sum_to_zero(list_of_integers: List[int]) -> bool:
    length = len(list_of_integers)
    for index_one in range(length - 1):
        first_element = list_of_integers[index_one]
        for index_two in range(index_one + 1, length):
            if first_element + list_of_integers[index_two] == 0:
                return True
    return False