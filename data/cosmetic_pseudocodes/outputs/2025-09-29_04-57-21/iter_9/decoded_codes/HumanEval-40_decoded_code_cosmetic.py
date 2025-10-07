from typing import List

def triples_sum_to_zero(list_of_integers: List[int]) -> bool:
    length: int = len(list_of_integers)
    current_first: int = 0
    while current_first < length - 2:
        current_second: int = current_first + 1
        while current_second < length - 1:
            current_third: int = current_second + 1
            while current_third < length:
                if not (list_of_integers[current_first] + list_of_integers[current_second] + list_of_integers[current_third] != 0):
                    return True
                current_third += 1
            current_second += 1
        current_first += 1
    return False