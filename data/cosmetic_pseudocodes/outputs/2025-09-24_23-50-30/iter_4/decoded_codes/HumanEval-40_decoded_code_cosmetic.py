from typing import List

def triples_sum_to_zero(list_of_integers: List[int]) -> bool:
    n: int = len(list_of_integers)

    def search_triple(a: int, b: int, c: int) -> bool:
        if c >= n:
            if b + 1 < n:
                return search_triple(a, b + 1, b + 2)
            elif a + 1 < n - 1:
                return search_triple(a + 1, a + 2, a + 3)
            else:
                return False
        return (list_of_integers[a] + list_of_integers[b] + list_of_integers[c] == 0) or search_triple(a, b, c + 1)

    return search_triple(0, 1, 2)