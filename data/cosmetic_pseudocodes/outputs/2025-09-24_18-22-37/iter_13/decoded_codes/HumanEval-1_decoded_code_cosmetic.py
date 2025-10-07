from typing import List

def separate_paren_groups(string_of_parentheses: str) -> List[str]:
    result_collection: List[str] = []
    temp_string_collection: List[str] = []
    depth_counter: int = 0
    index_pointer: int = 0
    str_length: int = len(string_of_parentheses)

    while index_pointer < str_length:
        current_char: str = string_of_parentheses[index_pointer]
        if current_char not in ('(', ')'):
            index_pointer += 1
            continue

        if current_char == '(':
            depth_counter += 1
            temp_string_collection.append(current_char)
        else:
            depth_counter -= 1
            temp_string_collection.append(current_char)
            if depth_counter == 0:
                accumulated_string: str = ''.join(temp_string_collection)
                result_collection.append(accumulated_string)
                temp_string_collection.clear()
        index_pointer += 1

    return result_collection