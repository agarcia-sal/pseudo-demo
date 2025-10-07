from typing import List

def sort_array(array: List[int]) -> List[int]:
    if len(array) == 0:
        return []
    sum_first_last = array[0] + array[-1]
    is_even = (sum_first_last % 2) == 0
    array_copy = [x for x in array]

    if is_even:
        sorted_array: List[int] = []
        while len(array_copy) > 0:
            max_element = array_copy[0]
            max_index = 0
            for i in range(1, len(array_copy)):
                if array_copy[i] > max_element:
                    max_element = array_copy[i]
                    max_index = i
            sorted_array.append(max_element)
            array_copy.pop(max_index)
        return sorted_array
    else:
        sorted_array: List[int] = []
        while len(array_copy) > 0:
            min_element = array_copy[0]
            min_index = 0
            for i in range(1, len(array_copy)):
                if array_copy[i] < min_element:
                    min_element = array_copy[i]
                    min_index = i
            sorted_array.append(min_element)
            array_copy.pop(min_index)
        return sorted_array