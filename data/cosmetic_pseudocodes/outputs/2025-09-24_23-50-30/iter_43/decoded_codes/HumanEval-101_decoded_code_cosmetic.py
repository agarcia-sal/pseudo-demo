from typing import List


def words_string(present_string: str) -> List[str]:
    index_var: int = 0
    buffer_array: List[str] = []
    while index_var < len(present_string):
        if present_string[index_var] == ',':
            buffer_array.append(' ')
        else:
            buffer_array.append(present_string[index_var])
        index_var += 1
    combined_text: str = "".join(buffer_array)
    return combined_text.split()