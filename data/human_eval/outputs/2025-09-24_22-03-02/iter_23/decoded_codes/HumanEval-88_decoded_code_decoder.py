from typing import List

def sort_array(array: List[int]) -> List[int]:
    if len(array) == 0:
        return []
    else:
        s = array[0] + array[len(array) - 1]
        if s % 2 == 0:
            result = sorted(array, reverse=True)
        else:
            result = sorted(array, reverse=False)
        return result