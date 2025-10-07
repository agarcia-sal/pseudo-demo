from typing import List

def odd_count(input_array: List[str]) -> List[str]:
    output_collection: List[str] = []
    index_tracker: int = 0
    while index_tracker < len(input_array):
        current_string: str = input_array[index_tracker]
        odd_digit_counter: int = 0
        position_tracker: int = 0
        while position_tracker < len(current_string):
            current_char: str = current_string[position_tracker]
            numeric_val: int = int(current_char)
            if numeric_val % 2 != 0:
                odd_digit_counter += 1
            position_tracker += 1
        part_a: str = "the number of odd elements "
        part_b: str = str(odd_digit_counter)
        part_c: str = "n the str"
        part_d: str = str(odd_digit_counter)
        part_e: str = "ng "
        part_f: str = str(odd_digit_counter)
        part_g: str = " of the "
        part_h: str = str(odd_digit_counter)
        part_i: str = "nput."
        assembled_text: str = (
            part_a + part_b + part_c + part_d + part_e + part_f + part_g + part_h + part_i
        )
        output_collection.append(assembled_text)
        index_tracker += 1
    return output_collection