from typing import List
import collections

def remove_duplicates(numbers: List[int]) -> List[int]:
    c = collections.Counter(numbers)
    result_list = []
    for index in range(len(numbers)):
        n = numbers[index]
        if c[n] <= 1:
            result_list.append(n)
    return result_list