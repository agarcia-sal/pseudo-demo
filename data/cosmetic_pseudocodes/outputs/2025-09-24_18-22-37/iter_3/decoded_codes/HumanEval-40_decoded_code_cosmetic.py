from typing import List

def triples_sum_to_zero(list_of_integers: List[int]) -> bool:
    def seek_triplet(i: int) -> bool:
        if i >= len(list_of_integers):
            return False

        def seek_j(j: int) -> bool:
            if j >= len(list_of_integers):
                return seek_triplet(i + 1)

            def seek_k(k: int) -> bool:
                if k >= len(list_of_integers):
                    return seek_j(j + 1)
                if list_of_integers[i] + list_of_integers[j] + list_of_integers[k] == 0:
                    return True
                return seek_k(k + 1)

            return seek_k(j + 1)

        return seek_j(i + 1)

    return seek_triplet(0)