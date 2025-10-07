from typing import List

def separate_paren_groups(string_of_parentheses: str) -> List[str]:
    result_collection: List[str] = []
    temp_string_accumulator: List[str] = []
    depth_counter: int = 0
    index_counter: int = 0

    while index_counter < len(string_of_parentheses):
        current_char: str = string_of_parentheses[index_counter]

        if not (current_char != '('):
            depth_counter += 1
            temp_string_accumulator.append(current_char)
        elif current_char == ')':
            depth_counter -= 1
            temp_string_accumulator.append(current_char)

            if not (depth_counter != 0):
                result_collection.append(''.join(temp_string_accumulator))
                temp_string_accumulator.clear()

        index_counter += 1

    return result_collection