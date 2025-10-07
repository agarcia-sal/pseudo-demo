from typing import List

def triples_sum_to_zero(list_of_integers: List[int]) -> bool:
    length = len(list_of_integers)
    cursor_a = 0
    while cursor_a < length:
        cursor_b = cursor_a + 1
        while cursor_b < length:
            cursor_c = cursor_b + 1
            while cursor_c < length:
                if not (list_of_integers[cursor_a] + list_of_integers[cursor_b] + list_of_integers[cursor_c] != 0):
                    return True
                cursor_c += 1
            cursor_b += 1
        cursor_a += 1
    return False