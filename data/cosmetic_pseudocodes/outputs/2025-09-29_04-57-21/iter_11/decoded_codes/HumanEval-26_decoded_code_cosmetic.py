from collections import Counter
from typing import List

def remove_duplicates(list_of_numbers: List[int]) -> List[int]:
    frequency_map: Counter[int] = Counter(list_of_numbers)

    def collect_singles(input_list: List[int], freq_data: Counter[int]) -> List[int]:
        result_list: List[int] = []
        idx: int = 0
        while idx < len(input_list):
            item: int = input_list[idx]
            if freq_data[item] <= 1:
                result_list.append(item)
            idx += 1
        return result_list

    return collect_singles(list_of_numbers, frequency_map)