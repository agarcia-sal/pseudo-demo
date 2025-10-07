from typing import List

def triples_sum_to_zero(list_of_integers: List[int]) -> bool:
    def recursive_i(i: int) -> bool:
        if i >= len(list_of_integers) - 2:
            return False

        def recursive_j(j: int) -> bool:
            if j >= len(list_of_integers) - 1:
                return recursive_i(i + 1)

            def recursive_k(k: int) -> bool:
                if k >= len(list_of_integers):
                    return recursive_j(j + 1)

                if list_of_integers[i] + list_of_integers[j] + list_of_integers[k] == 0:
                    return True
                return recursive_k(k + 1)

            return recursive_k(j + 1)

        return recursive_j(i + 1)

    return recursive_i(0)