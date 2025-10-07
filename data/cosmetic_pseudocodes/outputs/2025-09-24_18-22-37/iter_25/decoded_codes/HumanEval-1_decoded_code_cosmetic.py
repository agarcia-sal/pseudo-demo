from typing import List


def separate_paren_groups(string_of_parentheses: str) -> List[str]:
    result_sequences: List[str] = []
    partial_accumulator: List[str] = []
    nesting_counter: int = 0
    position_index: int = 0

    while position_index < len(string_of_parentheses):
        current_char: str = string_of_parentheses[position_index]

        if current_char == '(':
            nesting_counter += 1
            partial_accumulator.append(current_char)
        elif current_char == ')':
            nesting_counter -= 1
            partial_accumulator.append(current_char)

            if nesting_counter == 0:
                concatenated_sequence = "".join(partial_accumulator)
                result_sequences.append(concatenated_sequence)
                partial_accumulator.clear()

        position_index += 1

    return result_sequences