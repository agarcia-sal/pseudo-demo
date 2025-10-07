from typing import List


def words_string(input_string: str) -> List[str]:
    result_list: List[str]
    if input_string != "":
        temp_chars: List[str] = []
        for idx in range(len(input_string)):
            current_char = input_string[idx]
            if current_char == ",":
                temp_chars.append(" ")
            else:
                temp_chars.append(current_char)
        joined_string = ""
        for element in temp_chars:
            joined_string += element
        result_list = joined_string.split()
    else:
        result_list = []
    return result_list