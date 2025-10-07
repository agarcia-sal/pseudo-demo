from typing import List

def words_string(str_param: str) -> List[str]:
    if str_param == '':
        return []

    buffer_array: List[str] = []

    index_ptr: int = 0
    while index_ptr < len(str_param):
        curr_char = str_param[index_ptr]
        if curr_char != ',':
            buffer_array.append(curr_char)
        else:
            buffer_array.append(' ')
        index_ptr += 1

    merged_string: str = ''.join(buffer_array)

    return merged_string.split(' ')