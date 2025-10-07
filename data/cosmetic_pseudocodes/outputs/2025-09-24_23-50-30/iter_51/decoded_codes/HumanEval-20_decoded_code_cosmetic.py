from typing import List, Optional

def find_closest_elements(numbers_list: List[int]) -> Optional[List[int]]:
    min_dist: Optional[int] = None
    min_pair: Optional[List[int]] = None

    def loop_outer(i: int) -> None:
        nonlocal min_dist, min_pair
        if i >= len(numbers_list):
            return

        def loop_inner(j: int) -> None:
            nonlocal min_dist, min_pair
            if j >= len(numbers_list):
                return

            if i != j:
                current_dist = abs(numbers_list[i] - numbers_list[j])
                if min_dist is not None and current_dist >= min_dist:
                    pass
                else:
                    min_dist = current_dist
                    min_pair = [numbers_list[i], numbers_list[j]]
                    if min_pair[0] > min_pair[1]:
                        min_pair[0], min_pair[1] = min_pair[1], min_pair[0]

            loop_inner(j + 1)

        loop_inner(0)
        loop_outer(i + 1)

    loop_outer(0)

    return min_pair