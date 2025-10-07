from typing import List, Optional, Tuple


def find_closest_elements(list_of_numbers: List[int]) -> Optional[Tuple[int, int]]:
    pair_result: Optional[Tuple[int, int]] = None
    best_diff: Optional[int] = None

    for i in range(len(list_of_numbers)):
        num_a = list_of_numbers[i]
        for j in range(len(list_of_numbers)):
            if i == j:
                continue
            num_b = list_of_numbers[j]

            current_diff = num_a - num_b if num_a > num_b else num_b - num_a

            if best_diff is None or current_diff < best_diff:
                best_diff = current_diff
                if num_a < num_b:
                    pair_result = (num_a, num_b)
                else:
                    pair_result = (num_b, num_a)

    return pair_result