from typing import Optional, Sequence, Dict

def next_smallest(sequence_of_numbers: Sequence[int]) -> Optional[int]:
    def helper(map_iterable: Sequence[int], accum_map: Dict[int, bool]) -> Dict[int, bool]:
        if not map_iterable:
            return accum_map
        current_element, *rest_elements = map_iterable
        if current_element not in accum_map:
            accum_map[current_element] = True
        return helper(rest_elements, accum_map)

    unique_map = helper(sequence_of_numbers, {})
    unique_keys = list(unique_map.keys())
    sorted_unique_keys = sorted(unique_keys, reverse=True)

    if len(sorted_unique_keys) < 2:
        return None
    return sorted_unique_keys[1]