from typing import List

def triples_sum_to_zero(list_of_integers: List[int]) -> bool:
    def recursive_check(a: int, b: int, c: int) -> bool:
        n = len(list_of_integers)
        if a >= n - 2:
            return False
        elif b >= n - 1:
            return recursive_check(a + 1, a + 2, a + 3)
        elif c >= n:
            return recursive_check(a, b + 1, b + 2)
        elif list_of_integers[a] + list_of_integers[b] + list_of_integers[c] == 0:
            return True
        else:
            return recursive_check(a, b, c + 1)

    return recursive_check(0, 1, 2)