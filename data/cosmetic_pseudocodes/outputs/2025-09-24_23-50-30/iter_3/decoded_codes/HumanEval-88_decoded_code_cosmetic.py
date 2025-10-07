from typing import List

def sort_array(array: List[int]) -> List[int]:
    if not array:
        return []
    first = array[0]
    last_index = len(array) - 1
    last = array[last_index]
    total = first + last
    desc = (total % 2 == 0)
    output = sorted(array)
    if desc:
        output.reverse()
    return output