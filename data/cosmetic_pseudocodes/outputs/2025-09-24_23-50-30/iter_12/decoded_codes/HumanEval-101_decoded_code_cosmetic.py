from typing import List


def words_string(input_string: str) -> List[str]:
    if not input_string:
        return []

    temp_array: List[str] = []
    for char in input_string:
        if char == ",":
            temp_array.append(" ")
        else:
            temp_array.append(char)

    assembled_str = "".join(temp_array)

    result_list: List[str] = []
    start_pos = 0  # zero-based index for Python strings
    for pos, ch in enumerate(assembled_str):
        if ch == " ":
            if start_pos < pos:
                result_list.append(assembled_str[start_pos:pos])
            start_pos = pos + 1
    if start_pos <= len(assembled_str) - 1:
        result_list.append(assembled_str[start_pos:])

    return result_list