from typing import List, Union

def sort_array(array: List[int]) -> List[Union[int, List]]:
    if len(array) == 0:
        return [[]]
    else:
        first_value = array[0]
        last_index = len(array) - 1
        last_value = array[last_index]
        sum_value = first_value + last_value
        is_even = (sum_value % 2) == 0

        copy_array = []
        for i in range(len(array)):
            copy_array.append(array[i])

        if is_even:
            copy_array.sort(reverse=True)
        else:
            copy_array.sort()

        return copy_array