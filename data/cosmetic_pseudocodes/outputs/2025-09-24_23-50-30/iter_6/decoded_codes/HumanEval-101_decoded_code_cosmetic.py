from typing import List

def words_string(input_string: str) -> List[str]:
    result_list: List[str] = []
    if input_string:
        index = 0
        while index < len(input_string):
            current_char = input_string[index]
            if current_char != ',':
                result_list.append(current_char)
            else:
                result_list.append(' ')
            index += 1
    combined_str = "".join(result_list)
    return combined_str.split()