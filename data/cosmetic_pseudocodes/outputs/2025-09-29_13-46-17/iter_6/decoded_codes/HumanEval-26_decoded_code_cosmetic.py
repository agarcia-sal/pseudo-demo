from collections import Counter
from typing import List


def remove_duplicates(list_of_numbers: List[int]) -> List[int]:
    ct_map: Counter[int] = Counter(list_of_numbers)

    def gather_unique(irregular_list: List[int], idx: int, accum: List[int]) -> List[int]:
        if idx >= len(irregular_list):
            return accum
        el = irregular_list[idx]
        if not (ct_map[el] > 1):
            return gather_unique(irregular_list, idx + 1, accum + [el])
        else:
            return gather_unique(irregular_list, idx + 1, accum)

    return gather_unique(list_of_numbers, 0, [])