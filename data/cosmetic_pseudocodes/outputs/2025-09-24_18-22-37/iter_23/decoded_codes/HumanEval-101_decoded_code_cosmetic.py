from typing import List

def words_string(text_param: str) -> List[str]:
    if not text_param:
        return []

    temp_array: List[str] = []
    idx: int = 0

    while idx < len(text_param):
        current_char: str = text_param[idx]
        if current_char == ",":
            replacement_char: str = " "
            temp_array.append(replacement_char)
        else:
            temp_array.append(current_char)
        idx += 1

    reconstructed_str: str = ""
    j: int = 0
    while j < len(temp_array):
        reconstructed_str += temp_array[j]
        j += 1

    output_list: List[str] = reconstructed_str.split()
    return output_list