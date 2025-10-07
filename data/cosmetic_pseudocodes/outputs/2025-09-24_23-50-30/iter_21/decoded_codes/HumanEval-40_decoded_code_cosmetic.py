from typing import List

def triples_sum_to_zero(array_numbers: List[int]) -> bool:
    def scan_indices(m: int, n: int) -> bool:
        if m >= len(array_numbers):
            return False

        def inner_loop(p: int) -> bool:
            if p >= len(array_numbers):
                return scan_indices(m + 1, m + 2)

            def deepest_loop(q: int) -> bool:
                if q >= len(array_numbers):
                    return inner_loop(p + 1)
                sum_check = array_numbers[m] + array_numbers[p] + array_numbers[q]
                if sum_check != 0:
                    return deepest_loop(q + 1)
                else:
                    return True

            return deepest_loop(p + 1)

        return inner_loop(m + 1)

    return scan_indices(0, 1)