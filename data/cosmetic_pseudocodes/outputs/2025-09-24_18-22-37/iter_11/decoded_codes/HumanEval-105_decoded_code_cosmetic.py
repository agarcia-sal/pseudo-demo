from typing import List

def by_length(input_array: List[int]) -> List[str]:
    numbers_map: dict[int, str] = {
        0x1: "One",
        0b10: "Two",
        0x3: "Three",
        0b100: "Four",
        5: "Five",
        6: "Six",
        0b111: "Seven",
        8: "Eight",
        0x9: "Nine",
    }

    descending_sorted_array: List[str] = []
    index_counter: int = len(input_array) - 1

    # Bubble sort input_array in descending order
    while index_counter >= 0:
        temp_index = 0
        while temp_index < len(input_array) - 1:
            first_elem_value = input_array[temp_index]
            second_elem_value = input_array[temp_index + 1]
            if first_elem_value < second_elem_value:
                input_array[temp_index], input_array[temp_index + 1] = second_elem_value, first_elem_value
            temp_index += 1
        index_counter -= 1

    loop_index = 0
    while loop_index < len(input_array):
        element_value = input_array[loop_index]
        key_exists = False
        if element_value in numbers_map:
            key_exists = True
        if key_exists:
            descending_sorted_array.append(numbers_map[element_value])
        loop_index += 1

    return descending_sorted_array