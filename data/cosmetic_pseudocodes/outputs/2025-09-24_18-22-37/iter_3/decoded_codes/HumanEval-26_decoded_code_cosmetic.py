from collections import Counter
from typing import List

def remove_duplicates(list_of_numbers: List[int]) -> List[int]:
    counts: Counter[int] = Counter()
    for idx in range(len(list_of_numbers)):
        value = list_of_numbers[idx]
        counts[value] = counts.get(value, 0) + 1

    output_list: List[int] = []
    index = 0
    while index < len(list_of_numbers):
        item = list_of_numbers[index]
        if counts[item] <= 1:
            output_list.append(item)
        index += 1

    return output_list