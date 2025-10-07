from typing import List, Optional, Dict


def next_smallest(numbers: List[int]) -> Optional[int]:
    def extract_second_element(collection: List[int], idx: int) -> Optional[int]:
        if idx == len(collection):
            return None
        elif idx == 1:
            return collection[idx]
        else:
            return extract_second_element(collection, idx + 1)

    elements_map: Dict[int, bool] = {}
    for num in numbers:
        elements_map[num] = True

    sorted_keys: List[int] = []
    for key in elements_map:
        sorted_keys.append(key)

    sorted_keys = sorted(sorted_keys)

    return extract_second_element(sorted_keys, 0)