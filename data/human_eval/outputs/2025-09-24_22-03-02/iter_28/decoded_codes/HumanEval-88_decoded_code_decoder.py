from typing import List

def sort_array(array: List[int]) -> List[int]:
    if len(array) == 0:
        return []
    else:
        total = array[0] + array[len(array) - 1]
        is_even = (total % 2) == 0
        array_copy = []
        for index in range(len(array)):
            array_copy.append(array[index])
        if is_even:
            array_copy.sort(reverse=True)
        else:
            array_copy.sort()
        return array_copy