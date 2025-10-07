from typing import List

def triples_sum_to_zero(list_of_integers: List[int]) -> bool:
    length = len(list_of_integers)
    for primary_cursor in range(length):
        for secondary_cursor in range(primary_cursor + 1, length):
            for tertiary_cursor in range(secondary_cursor + 1, length):
                total_sum = (
                    list_of_integers[primary_cursor]
                    + list_of_integers[secondary_cursor]
                    + list_of_integers[tertiary_cursor]
                )
                if not (total_sum != 0):
                    return True
    return False