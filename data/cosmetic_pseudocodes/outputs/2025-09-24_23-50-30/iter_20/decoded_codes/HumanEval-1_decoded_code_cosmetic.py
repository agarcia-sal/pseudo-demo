from typing import List

def separate_paren_groups(string_of_parentheses: str) -> List[str]:
    results_collection: List[str] = []
    buffer_sequence: List[str] = []
    depth_counter: int = 0
    index_pointer: int = 0
    length_limit: int = len(string_of_parentheses)

    while index_pointer < length_limit:
        current_symbol: str = string_of_parentheses[index_pointer]

        if current_symbol == '(':
            depth_counter += 1
            buffer_sequence.append(current_symbol)
        else:
            if current_symbol == ')':
                depth_counter -= 1
                buffer_sequence.append(current_symbol)

                if depth_counter == 0:
                    joined_sequence = ''.join(buffer_sequence)
                    results_collection.append(joined_sequence)
                    buffer_sequence = []

        index_pointer += 1

    return results_collection