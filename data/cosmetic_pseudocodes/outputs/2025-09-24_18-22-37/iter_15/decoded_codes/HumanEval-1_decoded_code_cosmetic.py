from typing import List


def separate_paren_groups(input_sequence: str) -> List[str]:
    accumulator: List[str] = []
    buffer: List[str] = []
    depth_counter: int = 0
    index_counter: int = 0
    sequence_length: int = len(input_sequence)

    while index_counter < sequence_length:
        current_element: str = input_sequence[index_counter]

        if current_element == '(':
            depth_counter += 1
            buffer.append(current_element)
        elif current_element == ')':
            depth_counter -= 1
            buffer.append(current_element)
            if depth_counter == 0:
                combined_string = ''.join(buffer)
                accumulator.append(combined_string)
                buffer.clear()
        # default: no action

        index_counter += 1

    return accumulator