from typing import Optional, Sequence, Tuple


def find_closest_elements(numbers_collection: Sequence[int]) -> Optional[Tuple[int, int]]:
    best_match: Optional[Tuple[int, int]] = None
    smallest_gap: Optional[int] = None

    length = len(numbers_collection)
    for posA in range(length):
        valA = numbers_collection[posA]
        posB = 0
        while posB < length:
            valB = numbers_collection[posB]
            if posA == posB:
                pass  # skip same indices
            else:
                diff = valA - valB
                abs_diff = diff if diff >= 0 else -diff
                if smallest_gap is None:
                    smallest_gap = abs_diff
                    pair_list = [valA, valB]
                    if pair_list[0] > pair_list[1]:
                        pair_list[0], pair_list[1] = pair_list[1], pair_list[0]
                    best_match = (pair_list[0], pair_list[1])
                else:
                    if abs_diff < smallest_gap:
                        smallest_gap = abs_diff
                        sorted_pair = [valA, valB]
                        if sorted_pair[0] > sorted_pair[1]:
                            sorted_pair[0], sorted_pair[1] = sorted_pair[1], sorted_pair[0]
                        best_match = (sorted_pair[0], sorted_pair[1])
            posB += 1

    return best_match