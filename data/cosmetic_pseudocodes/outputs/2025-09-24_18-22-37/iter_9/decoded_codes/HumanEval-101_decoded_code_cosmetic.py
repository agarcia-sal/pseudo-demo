from typing import List

def words_string(str_param: str) -> List[str]:
    if not str_param:
        return []
    temp_array: List[str] = []
    for idx in range(len(str_param)):
        current_char = str_param[idx]
        if current_char == ',':
            temp_array.append(' ')
        else:
            temp_array.append(current_char)
    combined_string = ''.join(temp_array)
    words_result = combined_string.split(' ')
    return words_result