from typing import List

def strange_sort_list(array_of_numbers: List[int]) -> List[int]:
    output_array: List[int] = []
    toggle: bool = False
    while len(array_of_numbers) > 0:
        toggle = not toggle
        if not toggle:
            lowest_value = array_of_numbers[0]
            index_of_lowest = 0
            for i in range(1, len(array_of_numbers)):
                if array_of_numbers[i] < lowest_value:
                    lowest_value = array_of_numbers[i]
                    index_of_lowest = i
            output_array.append(lowest_value)
            del array_of_numbers[index_of_lowest]
        else:
            highest_value = array_of_numbers[0]
            index_of_highest = 0
            for j in range(1, len(array_of_numbers)):
                if array_of_numbers[j] > highest_value:
                    highest_value = array_of_numbers[j]
                    index_of_highest = j
            output_array.append(highest_value)
            del array_of_numbers[index_of_highest]
    return output_array