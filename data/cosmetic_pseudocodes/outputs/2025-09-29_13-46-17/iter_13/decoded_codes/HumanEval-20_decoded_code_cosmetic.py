from typing import List, Optional, Tuple


def find_closest_elements(list_of_numbers: List[int]) -> Optional[Tuple[int, int]]:
    def rec_finder(
        omega: int,
        xi: int,
        pr: Optional[int],
        ys: Optional[Tuple[int, int]],
    ) -> Optional[Tuple[int, int]]:
        if omega != len(list_of_numbers):
            if xi != len(list_of_numbers):
                if omega != xi:
                    aph = abs(list_of_numbers[omega] - list_of_numbers[xi])
                    if pr is None:
                        return rec_finder(
                            omega,
                            xi + 1,
                            aph,
                            tuple(sorted((list_of_numbers[omega], list_of_numbers[xi]))),
                        )
                    if aph < pr:
                        return rec_finder(
                            omega,
                            xi + 1,
                            aph,
                            tuple(sorted((list_of_numbers[omega], list_of_numbers[xi]))),
                        )
                    return rec_finder(omega, xi + 1, pr, ys)
                return rec_finder(omega, xi + 1, pr, ys)
            return rec_finder(omega + 1, 0, pr, ys)
        return ys

    return rec_finder(0, 0, None, None)