from typing import List, Optional, Tuple


def find_closest_elements(list_of_numbers: List[int]) -> Optional[Tuple[int, int]]:
    e0: int = 0
    r0: Optional[Tuple[int, int]] = None
    r1: Optional[Tuple[int, int]] = None
    r2: Optional[int] = None

    while e0 < len(list_of_numbers):
        e1: int = 0
        while e1 < len(list_of_numbers):
            if e0 == e1:
                pass  # Skip same indices
            else:
                if r2 is None:
                    r2 = abs(list_of_numbers[e0] - list_of_numbers[e1])
                    r1 = (list_of_numbers[e0], list_of_numbers[e1])
                    r0 = (min(r1[0], r1[1]), max(r1[0], r1[1]))
                else:
                    s0 = abs(list_of_numbers[e0] - list_of_numbers[e1])
                    if s0 < r2:
                        r2 = s0
                        r1 = (list_of_numbers[e0], list_of_numbers[e1])
                        r0 = (min(r1[0], r1[1]), max(r1[0], r1[1]))
            e1 += 1
        e0 += 1

    return r0