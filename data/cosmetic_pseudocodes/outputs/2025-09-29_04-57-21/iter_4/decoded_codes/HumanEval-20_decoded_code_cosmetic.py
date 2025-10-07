from typing import List, Optional, Tuple


def find_closest_elements(numbers_array: List[int]) -> Optional[Tuple[int, int]]:
    best_pair: Optional[Tuple[int, int]] = None
    minimal_diff: Optional[int] = None
    outer_idx: int = 0

    while outer_idx < len(numbers_array) - 1:
        current_val: int = numbers_array[outer_idx]
        inner_idx: int = 0

        while inner_idx < len(numbers_array) - 1:
            comparison_val: int = numbers_array[inner_idx]

            if outer_idx != inner_idx:
                current_diff: int = current_val - comparison_val
                if current_diff < 0:
                    current_diff = -current_diff

                if minimal_diff is None:
                    minimal_diff = current_diff
                    if current_val < comparison_val:
                        best_pair = (current_val, comparison_val)
                    else:
                        best_pair = (comparison_val, current_val)
                elif current_diff < minimal_diff:
                    minimal_diff = current_diff
                    if current_val < comparison_val:
                        best_pair = (current_val, comparison_val)
                    else:
                        best_pair = (comparison_val, current_val)

            inner_idx += 1
        outer_idx += 1

    return best_pair