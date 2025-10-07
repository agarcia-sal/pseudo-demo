from typing import List, Optional, Tuple


def find_closest_elements(list_of_numbers: List[int]) -> Optional[Tuple[int, int]]:
    answer: Optional[Tuple[int, int]] = None
    best_dist: Optional[int] = None

    def helper(indices: List[int]) -> None:
        if not indices:
            return
        i = indices[0]
        tail_indices = indices[1:]

        def inner_loop(j_indices: List[int]) -> None:
            nonlocal answer, best_dist
            if not j_indices:
                return
            j = j_indices[0]
            if i != j:
                diff = list_of_numbers[i] - list_of_numbers[j]
                dist = diff if diff >= 0 else -diff
                if best_dist is None or dist < best_dist:
                    best_dist = dist
                    # Store pair with smaller element first
                    if list_of_numbers[i] < list_of_numbers[j]:
                        answer = (list_of_numbers[i], list_of_numbers[j])
                    else:
                        answer = (list_of_numbers[j], list_of_numbers[i])
            inner_loop(j_indices[1:])

        inner_loop(list(range(len(list_of_numbers))))
        helper(tail_indices)

    helper(list(range(len(list_of_numbers))))
    return answer