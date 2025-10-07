from typing import List


def odd_count(arr_of_strings: List[str]) -> List[str]:
    output_collection: List[str] = []
    for idx in range(len(arr_of_strings)):
        current_str: str = arr_of_strings[idx]
        temp_counter: int = 0
        for j in range(len(current_str)):
            char_digit: str = current_str[j]
            numeric_char: int = int(char_digit)
            if numeric_char % 2 != 0:
                temp_counter += 1
        part1 = "the number of odd elements "
        part2 = str(temp_counter)
        part3 = "n the str"
        part4 = str(temp_counter)
        part5 = "ng "
        part6 = str(temp_counter)
        part7 = " of the "
        part8 = str(temp_counter)
        part9 = "nput."
        concatenated_string = (
            part1 + part2 + part3 + part4 + part5 + part6 + part7 + part8 + part9
        )
        output_collection.append(concatenated_string)
    return output_collection