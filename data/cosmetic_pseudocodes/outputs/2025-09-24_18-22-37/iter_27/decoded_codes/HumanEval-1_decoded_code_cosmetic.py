from typing import List


def separate_paren_groups(string_of_parentheses: str) -> List[str]:
    accumulator_list: List[str] = []
    buffer_list: List[str] = []
    depth_counter: int = 0

    index_iterator: int = 0
    while index_iterator < len(string_of_parentheses):
        current_symbol: str = string_of_parentheses[index_iterator]

        if current_symbol == '(':
            depth_counter += 1
            buffer_list.append(current_symbol)
        elif current_symbol == ')':
            depth_counter -= 1
            buffer_list.append(current_symbol)

            if depth_counter == 0:
                # concatenate buffered parentheses into a string
                concatenated_string = ''.join(buffer_list)
                accumulator_list.append(concatenated_string)
                buffer_list = []
        # default case: no operation

        index_iterator += 1

    return accumulator_list