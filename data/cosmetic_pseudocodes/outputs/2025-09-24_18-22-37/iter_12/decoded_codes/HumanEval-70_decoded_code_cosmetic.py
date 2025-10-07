from typing import List

def strange_sort_list(array_of_numbers: List[int]) -> List[int]:
    output_array: List[int] = []
    toggle_boolean: bool = False
    numbers = array_of_numbers.copy()  # avoid mutating the input list

    for _ in range(len(numbers)):
        if not toggle_boolean:
            temp_value = min(numbers)
        else:
            temp_value = max(numbers)

        output_array.append(temp_value)

        # Find first occurrence index of temp_value
        index_to_remove = 0
        for idx, val in enumerate(numbers):
            if val == temp_value:
                index_to_remove = idx
                break

        numbers.pop(index_to_remove)
        toggle_boolean = not toggle_boolean

    return output_array