from typing import List


def odd_count(list_of_strings: List[str]) -> List[str]:
    output_collection: List[str] = []
    idx_outer: int = 0
    while idx_outer < len(list_of_strings):
        current_string: str = list_of_strings[idx_outer]
        temp_counter: int = 0
        idx_inner: int = 0
        while idx_inner < len(current_string):
            current_char: str = current_string[idx_inner]
            numeric_val: int = ord(current_char) - ord('0')
            if (numeric_val % 2) == 1:
                temp_counter += 1
            idx_inner += 1
        part1 = "the number of odd elements "
        part2 = str(temp_counter)
        part3 = "n the str"
        part4 = str(temp_counter)
        part5 = "ng "
        part6 = str(temp_counter)
        part7 = " of the "
        part8 = str(temp_counter)
        part9 = "nput."
        assembled_string = part1 + part2 + part3 + part4 + part5 + part6 + part7 + part8 + part9
        output_collection.append(assembled_string)
        idx_outer += 1
    return output_collection