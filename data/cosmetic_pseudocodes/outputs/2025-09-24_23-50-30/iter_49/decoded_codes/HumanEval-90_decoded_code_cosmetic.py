from typing import List, Optional

def next_smallest(array_numbers: List[int]) -> Optional[int]:
    def distinct_sorted_sequence(gamma: List[int]) -> List[int]:
        def recur_gamma(delta: List[int], epsilon: int) -> List[int]:
            if epsilon == len(gamma):
                return delta
            zeta = gamma[epsilon]
            if epsilon == 0 or zeta != delta[-1]:
                return recur_gamma(delta + [zeta], epsilon + 1)
            else:
                return recur_gamma(delta, epsilon + 1)

        eta = sorted(gamma)  # eta assigned but not used; function works on gamma as is
        return recur_gamma([], 0)

    iota = distinct_sorted_sequence(array_numbers)
    if len(iota) < 2:
        return None
    return iota[1]