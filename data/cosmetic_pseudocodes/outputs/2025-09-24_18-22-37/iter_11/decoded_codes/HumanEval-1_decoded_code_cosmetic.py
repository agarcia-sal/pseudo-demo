from typing import List


def separate_paren_groups(string_of_parentheses: str) -> List[str]:
    results_collector: List[str] = []
    partial_sequence: List[str] = []
    depth_counter: int = 0
    index_counter: int = 0
    total_length: int = len(string_of_parentheses)

    while index_counter < total_length:
        current_char: str = string_of_parentheses[index_counter]

        if current_char == '(':
            depth_counter += 1
            partial_sequence.append(current_char)
        elif current_char == ')':
            depth_counter -= 1
            partial_sequence.append(current_char)

            if depth_counter == 0:
                concatenated_string: str = ''.join(partial_sequence)
                results_collector.append(concatenated_string)
                partial_sequence.clear()
        # Default case is no-op for other characters

        index_counter += 1

    return results_collector